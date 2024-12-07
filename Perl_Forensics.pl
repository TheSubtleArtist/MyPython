#!/usr/bin/perl
#
# prefhashcalc.pl v0.1, written by Hexacorn.com, 2012-06
#
# The script calculates Prefetch file names for a given path for a couple
# of common Windows versions
#  - Windows XP 32-bit
#  - Windows Vista 32-bit
#  - Windows 7 32-bit
#  - Windows 7 64-bit
#  - Windows Server 2003 32-bit
#  - Windows Server 2008 32-bit
#  - Windows Server 2008 64-bit
#
# Usage:
#     prefhashcalc.pl <path> " <command line>"
#
# OR
#
#     prefhashcalc.pl <filelist>
#     where filelist contians rows with path, command line, description separated by |
#     e.g.
#     \WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL ncpa.cpl|Network Connections
#
# OR
#
#     prefhashcalc.pl <path+command line>
#
#
# If you find any bugs please let me know

use strict;
use warnings;
use bignum;

$|=1;

print STDERR "
======================================================================
 prefhashcalc v0.1, written by Hexacorn.com, 2012-06
======================================================================
Prefetch hash calculator, and lookup table generator

";


my $arg1 = shift;
my $arg2 = shift;

if (!defined($arg1))
{
  show_all_known();
}
else
{
   $arg2 = '' if !defined ($arg2);
   if ($arg1 =~ /^[-\/]f$/i)
   {
    print STDERR "Procesing '$arg2'\n";
    open F,"<$arg2" || die ("\nCan't open '$arg2'\n");
    binmode F;
    while (<F>)
    {
        s/[\r\n]+//;
        next if /^\s*$/;
        my @r=split(/\|/);
        next if !defined($r[0]);
        $r[1]='' if !defined($r[1]);
        $r[2]='' if !defined($r[2]);
        print STDOUT calc_prefetch_xp    ($r[0],$r[1],'XP    (32-bit)'.$r[2]);
        print STDOUT calc_prefetch_vista ($r[0],$r[1],'Vista (32-bit)'.$r[2]);
        print STDOUT calc_prefetch_w7    ($r[0],$r[1],'W7    (32-bit)'.$r[2]);
        print STDOUT calc_prefetch_2k3   ($r[0],$r[1],'2003  (32-bit)'.$r[2]);
        print STDOUT calc_prefetch_2k8   ($r[0],$r[1],'2008  (32-bit)'.$r[2]);
        print STDOUT calc_prefetch_w7_64 ($r[0],$r[1],'W7    (64-bit)'.$r[2]);
    }
    close F;
   }
   else
   {
      print STDOUT calc_prefetch_xp    ($arg1,$arg2,'XP    (32-bit)');
      print STDOUT calc_prefetch_vista ($arg1,$arg2,'Vista (32-bit)');
      print STDOUT calc_prefetch_w7    ($arg1,$arg2,'W7    (32-bit)');
      print STDOUT calc_prefetch_2k3   ($arg1,$arg2,'2003  (32-bit)');
      print STDOUT calc_prefetch_2k8   ($arg1,$arg2,'2008  (32-bit)');
      print STDOUT calc_prefetch_w7_64 ($arg1,$arg2,'W7    (64-bit)');
   }
}

sub calc_prefetch_w7
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('A'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_w7($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|dllhost|mmc|svchost|taskhost)\.exe/i)
     {
      $hash = ( $hash + hash_w7(a2u('"'.$origpath.'"'.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

sub calc_prefetch_w7_64
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('A'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_w7($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|dllhost|mmc|svchost|taskhost)\.exe/i)
     {
      $hash = ( $hash + hash_w7(a2u($origpath.' '.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

sub calc_prefetch_2k8
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('B'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_w7($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|dllhost|mmc|svchost|taskhost)\.exe/i)
     {
     $hash = ( $hash + hash_w7(a2u($origpath.' '.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

sub calc_prefetch_vista
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('B'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_vista($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|mmc)\.exe/i)
     {
      $hash = ( $hash + hash_vista(a2u('"'.$origpath.'"'.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

sub calc_prefetch_xp
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('B'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_xp($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|mmc)\.exe/i)
     {
      $hash = ( $hash + hash_xp(a2u('"'.$origpath.'"'.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

sub calc_prefetch_2k3
{
  my $origpath = shift;
  my $cmdline  = shift;
  my $desc     = shift;

  die "\"$cmdline\" is not prefixed with at least one blank character\n"
      if ($cmdline ne '' & $cmdline !~ /^\s/);

  my $devpath = uc($origpath);
  my ($filename) = $devpath =~ /([^\\\/]+?)$/;
  $devpath =~ s#^([C-Z]):\\#sprintf("\\DEVICE\\HARDDISKVOLUME%s\\",ord($1)-ord('B'))#es;

  my $devpath_u = a2u($devpath);

  my $hash = hash_xp($devpath_u);
  if ($cmdline ne ''&&$origpath =~ /(rundll32|dllhost|mmc|svchost|taskhost)\.exe/i)
     {
      $hash = ( $hash + hash_xp(a2u($origpath.$cmdline)) ) % 4294967296;
     }

  return "$desc\t".sprintf("$filename-%08lX.pf",$hash)."\t$origpath\t$cmdline\t$devpath\n";
}

# 2003 - DLLHOST.EXE,MMC.EXE,RUNDLL32.EXE
# hash same as XP
#HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management\PrefetchParameters
#HostingAppList
#RootDirPath

sub hash_xp
{
  my $devpath_u = shift;
  my $hash = 0;
  for (my $i=0; $i<length($devpath_u); $i++)
  {
      my $char = ord(substr($devpath_u,$i,1));
      $hash = ( ($hash * 37) + $char ) % 4294967296;
      #print STDERR sprintf("%08lX",$hash).' '.substr($devpath_u,$i,1)."\n";
  }
  $hash = ($hash * 314159269) % 4294967296;

  $hash = 0x100000000-$hash if ($hash>0x80000000);
  $hash = (abs($hash) % 1000000007) % 4294967296;
  return $hash;
}

sub hash_vista
{
  my $devpath_u = shift;
  my $hash = 314159;
  for (my $i=0; $i<length($devpath_u); $i++)
  {
      my $char = ord(substr($devpath_u,$i,1));
      $hash = ( ($hash * 37) + $char ) % 4294967296;
  }
  return $hash;
}

# PfCalculateProcessHash
# PfSnIsHostingApplication
# PfSnScanCommandLine
sub hash_w7
{
  my $devpath_u = shift;
  #print STDERR "devpath_u=\"$devpath_u\"\n";
  my $hash = 314159;
  my $numof8 = int(length($devpath_u)/8);
  for (my $i=0; $i<$numof8; $i++)
  {
      my $char0 = ord(substr($devpath_u,$i*8+0,1));
      my $char1 = ord(substr($devpath_u,$i*8+1,1));
      my $char2 = ord(substr($devpath_u,$i*8+2,1));
      my $char3 = ord(substr($devpath_u,$i*8+3,1));
      my $char4 = ord(substr($devpath_u,$i*8+4,1));
      my $char5 = ord(substr($devpath_u,$i*8+5,1));
      my $char6 = ord(substr($devpath_u,$i*8+6,1));
      my $char7 = ord(substr($devpath_u,$i*8+7,1));

      $hash = (442596621* $char0 +
              37*($char6 + 37*($char5 + 37*($char4 + 37*($char3 + 37*($char2 + 37*$char1)))))
              - 803794207*$hash + $char7) % 4294967296;
      #print STDERR sprintf("%08lX",$hash).' '.substr($devpath_u,$i*8,8)."\n";

  }
  for (my $k=0; $k<int(length($devpath_u) % 8); $k++)
  {
    $hash = (37*$hash+ord(substr($devpath_u,$numof8*8+$k,1)))  % 4294967296;
  }

  #print STDERR sprintf("%08lX",$hash)."\n";
  return $hash;
}

sub a2u
{
    my $string = shift;
    $string =~ s/(.)/$1\x00/gs;
    return $string;
}

sub show_all_known
{
       while (<DATA>)
       {
        s/[\r\n]+//;
        next if /^\s*$/;
        my @r=split(/\|/);
        next if !defined($r[0]);
        $r[1]='' if !defined($r[1]);
        $r[2]='' if !defined($r[2]);
        for (my $driven=ord('C'); $driven<=ord('F'); $driven++)
        {
           my $drive = chr($driven);
           print STDOUT calc_prefetch_xp    ($drive.':'.$r[0],$r[1],'XP    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_vista ($drive.':'.$r[0],$r[1],'Vista (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7    ($drive.':'.$r[0],$r[1],'W7    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k3   ($drive.':'.$r[0],$r[1],'2003  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k8   ($drive.':'.$r[0],$r[1],'2008  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7_64 ($drive.':'.$r[0],$r[1],'W7    (64-bit)'.$r[2]);

           next if $r[2] eq '';
           print STDOUT calc_prefetch_xp    (uc($drive).':'.$r[0],uc($r[1]),'XP    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_vista (uc($drive).':'.$r[0],uc($r[1]),'Vista (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7    (uc($drive).':'.$r[0],uc($r[1]),'W7    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k3   (uc($drive).':'.$r[0],uc($r[1]),'2003  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k8   (uc($drive).':'.$r[0],uc($r[1]),'2008  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7_64 (uc($drive).':'.$r[0],uc($r[1]),'W7    (64-bit)'.$r[2]);

           print STDOUT calc_prefetch_xp    (lc($drive).':'.$r[0],lc($r[1]),'XP    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_vista (lc($drive).':'.$r[0],lc($r[1]),'Vista (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7    (lc($drive).':'.$r[0],lc($r[1]),'W7    (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k3   (lc($drive).':'.$r[0],lc($r[1]),'2003  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_2k8   (lc($drive).':'.$r[0],lc($r[1]),'2008  (32-bit)'.$r[2]);
           print STDOUT calc_prefetch_w7_64 (lc($drive).':'.$r[0],lc($r[1]),'W7    (64-bit)'.$r[2]);
        }
       }
}

__DATA__

\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL main.cpl @0|Mouse Properties
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL wscui.cpl|Action Center
\WINDOWS\system32\rundll32.exe| shwebsvc.dll,AddNetPlaceRunDll|Add Network Location
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL appwiz.cpl|Add/Remove Programs
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL appwiz.cpl,,0|Add/Remove Programs
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL appwiz.cpl,,2|Add/Remove Windows Components
\WINDOWS\system32\rundll32.exe| DwmApi #104|Aero (Transparency feature) Off
\WINDOWS\system32\rundll32.exe| DwmApi #102|Aero (Transparency feature) On
\WINDOWS\system32\rundll32.exe| msrating.dll,RatingSetupUI|Content Advisor
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL|Control Panel
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL timedate.cpl|Date and Time
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL timedate.cpl,,1|Date and Time (Additional Clocks)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL timedate.cpl|Date and Time (Properties)
\WINDOWS\system32\rundll32.exe| devmgr.dll DeviceManager_Execute|Device Manager
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL hdwwiz.cpl|Device Manager
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL access.cpl,,3|Display Settings
\WINDOWS\system32\rundll32.exe| shell32.dll,Options_RunDLL 0|Folder Options
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_Options 2|Folder Options (File Types)
\WINDOWS\system32\rundll32.exe| shell32.dll,Options_RunDLL 2|Folder Options (Search)
\WINDOWS\system32\rundll32.exe| shell32.dll,Options_RunDLL 7|Folder Options (View)
\WINDOWS\system32\rundll32.exe| keymgr.dll,PRShowSaveWizardExW|Forgotten Password Wizard
\WINDOWS\system32\rundll32.exe| powrprof.dll,SetSuspendState|Hibernate
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL main.cpl @1|Keyboard Properties
\WINDOWS\system32\rundll32.exe| user32.dll,LockWorkStation|Lock Screen
\WINDOWS\system32\rundll32.exe| shell32.dll,SHHelpShortcuts_RunDLL Connect|Map Network Drive
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL main.cpl @0|Mouse Properties
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL ncpa.cpl|Network Connections
\WINDOWS\system32\rundll32.exe| shell32.dll,Options_RunDLL 5|Notification Cache
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL tabletpc.cpl|Pen and Touch Tablet PC (Settings)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL tabletpc.cpl,,1|Pen and Touch Tablet PC (Settings Flicks Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL tabletpc.cpl,,2|Pen and Touch Tablet PC (Settings Handwriting Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL collab.cpl|People Near Me
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL collab.cpl,,1|People Near Me (Sign Up Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL desk.cpl,,2|Personalization
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL telephon.cpl|Phone and Modem (Options)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL telephon.cpl,,1|Phone and Modem (Options Modems Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL telephon.cpl,,2|Phone and Modems (Options Advanced Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL powercfg.cpl|Power Options
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL powercfg.cpl,,1|Power Options Modify Plan Settings
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL intl.cpl,,3|Regional Settings
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL desk.cpl|Screen Resolution
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL desk.cpl,,1|ScreenSaver
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL appwiz.cpl,,3|Set Program Access and Computer Defaults
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLLmmsys.cpl|Sound Control Playback Tab
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLLmmsys.cpl,,1|Sound Control Recording Tab
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLLmmsys.cpl,,2|Sound Control Sounds Tab
\WINDOWS\system32\rundll32.exe| keymgr.dll,KRShowKeyMgr|Stored Usernames /Passwords
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl|System Properties
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,3|System Properties (Advanced Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,2|System Properties (Hardware Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,5|System Properties (Remote Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,4|System Properties (System Protection Tab)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,4|System Properties (Advanced)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL sysdm.cpl,,5|System Properties (Automatic Updates)
\WINDOWS\system32\rundll32.exe| shell32.dll,Options_RunDLL 1|Taskbar Properties
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL hotplug.dll|Unplug Eject Hardware
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL nusrmgr.cpl|User Accounts
\WINDOWS\system32\rundll32.exe| oobefldr.dll,ShowWelcomeCenter|Welcome Center
\WINDOWS\system32\rundll32.exe| SHELL32.DLL,ShellAboutW|Windows (About)
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL firewall.cpl|Windows Firewall
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL firewall.cpl|Windows Firewall
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL wscui.cpl|Windows Security Center
\WINDOWS\system32\rundll32.exe| shell32.dll,Control_RunDLL NetSetup.cpl,@0,WNSW|Wireless Network Setup
\WINDOWS\system32\rundll32.exe| van.dll,RunVAN|Wireless Networks pop-up
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 4351|Delete All (Deeper Cleaning Including Add-on Data Deletion)
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 255|Delete All
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 2|Delete Cookies
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 16|Delete Form Data
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 1|Delete History
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 32|Delete Passwords
\WINDOWS\system32\rundll32.exe| InetCpl.cpl,ClearMyTracksByProcess 8|Delete Temporary Internet Files

\windows\bfsvc.exe
\windows\bitlockerdiscoveryvolumecontents\bitlockertogo.exe
\windows\boot\pcat\memtest.exe
\windows\digitallocker\digitalx.exe
\windows\ehome\createdisc\sbeserver.exe
\windows\ehome\ehexthost.exe
\windows\ehome\ehmsas.exe
\windows\ehome\ehprivjob.exe
\windows\ehome\ehrec.exe
\windows\ehome\ehrecvr.exe
\windows\ehome\ehsched.exe
\windows\ehome\ehshell.exe
\windows\ehome\ehtray.exe
\windows\ehome\ehvid.exe
\windows\ehome\loadmxf.exe
\windows\ehome\mcglidhost.exe
\windows\ehome\mcrmgr.exe
\windows\ehome\mcspad.exe
\windows\ehome\mcupdate.exe
\windows\ehome\mcx2prov.exe
\windows\ehome\mcxtask.exe
\windows\ehome\mediacenterweblauncher.exe
\windows\ehome\registermceapp.exe
\windows\ehome\wtvconverter.exe
\windows\explorer.exe
\windows\fveupdate.exe
\windows\help\tablet pc\pentraining.exe
\windows\help\tablet pc\touchtraining.exe
\windows\help\tours\mmtour\tour.exe
\windows\helppane.exe
\windows\hh.exe
\windows\inf\unregmp2.exe
\windows\msagent\agentsvr.exe
\windows\mui\muisetup.exe
\windows\network diagnostic\xpnetdiag.exe
\windows\notepad.exe
\windows\panther\setup.exe
\windows\pchealth\helpctr\binaries\helpctr.exe
\windows\pchealth\helpctr\binaries\helphost.exe
\windows\pchealth\helpctr\binaries\helpsvc.exe
\windows\pchealth\helpctr\binaries\hscupd.exe
\windows\pchealth\helpctr\binaries\msconfig.exe
\windows\pchealth\helpctr\binaries\notiflag.exe
\windows\pchealth\uploadlb\binaries\uploadm.exe
\windows\regedit.exe
\windows\servicing\gc32\tzupd.exe
\windows\servicing\trustedinstaller.exe
\windows\servicing\vsp1ceip.exe
\windows\setup\scripts\bie7_inst.exe
\windows\setup\scripts\bie7_uninst.exe
\windows\setup\scripts\data\bootinst.exe
\windows\setup\scripts\data\editioncheck.exe
\windows\speech\common\sapisvr.exe
\windows\system32\accwiz.exe
\windows\system32\actmovie.exe
\windows\system32\acw.exe
\windows\system32\adaptertroubleshooter.exe
\windows\system32\ahui.exe
\windows\system32\aitagent.exe
\windows\system32\alg.exe
\windows\system32\append.exe
\windows\system32\appidcertstorecheck.exe
\windows\system32\appidpolicyconverter.exe
\windows\system32\arp.exe
\windows\system32\asr_fmt.exe
\windows\system32\asr_ldm.exe
\windows\system32\asr_pfu.exe
\windows\system32\at.exe
\windows\system32\atbroker.exe
\windows\system32\atmadm.exe
\windows\system32\attrib.exe
\windows\system32\audiodg.exe
\windows\system32\auditpol.exe
\windows\system32\auditusr.exe
\windows\system32\autochk.exe
\windows\system32\autoconv.exe
\windows\system32\autofmt.exe
\windows\system32\autolfn.exe
\windows\system32\axinstui.exe
\windows\system32\baaupdate.exe
\windows\system32\bcdboot.exe
\windows\system32\bcdedit.exe
\windows\system32\bdehdcfg.exe
\windows\system32\bdeuisrv.exe
\windows\system32\bdeunlockwizard.exe
\windows\system32\bitlockerwizard.exe
\windows\system32\bitlockerwizardelev.exe
\windows\system32\bitsadmin.exe
\windows\system32\blastcln.exe
\windows\system32\boot\winload.exe
\windows\system32\boot\winresume.exe
\windows\system32\bootcfg.exe
\windows\system32\bootok.exe
\windows\system32\bootvrfy.exe
\windows\system32\bridgeunattend.exe
\windows\system32\bthudtask.exe
\windows\system32\cacls.exe
\windows\system32\calc.exe
\windows\system32\cbsra.exe
\windows\system32\certenrollctrl.exe
\windows\system32\certreq.exe
\windows\system32\certutil.exe
\windows\system32\change.exe
\windows\system32\charmap.exe
\windows\system32\chglogon.exe
\windows\system32\chgport.exe
\windows\system32\chgusr.exe
\windows\system32\chkdsk.exe
\windows\system32\chkntfs.exe
\windows\system32\choice.exe
\windows\system32\cidaemon.exe
\windows\system32\cipher.exe
\windows\system32\cisvc.exe
\windows\system32\ckcnv.exe
\windows\system32\cleanmgr.exe
\windows\system32\cliconfg.exe
\windows\system32\clip.exe
\windows\system32\clipbrd.exe
\windows\system32\clipsrv.exe
\windows\system32\cmd.exe
\windows\system32\cmdkey.exe
\windows\system32\cmdl32.exe
\windows\system32\cmmon32.exe
\windows\system32\cmstp.exe
\windows\system32\cofire.exe
\windows\system32\colorcpl.exe
\windows\system32\com\comrepl.exe
\windows\system32\com\comrereg.exe
\windows\system32\com\migregdb.exe
\windows\system32\comp.exe
\windows\system32\compact.exe
\windows\system32\compmgmtlauncher.exe
\windows\system32\computerdefaults.exe
\windows\system32\conhost.exe
\windows\system32\conime.exe
\windows\system32\consent.exe
\windows\system32\control.exe
\windows\system32\convert.exe
\windows\system32\credwiz.exe
\windows\system32\cscript.exe
\windows\system32\csrss.exe
\windows\system32\csrstub.exe
\windows\system32\ctfmon.exe
\windows\system32\cttune.exe
\windows\system32\cttunesvr.exe
\windows\system32\dccw.exe
\windows\system32\dcomcnfg.exe
\windows\system32\ddeshare.exe
\windows\system32\ddodiag.exe
\windows\system32\debug.exe
\windows\system32\defrag.exe
\windows\system32\devicedisplayobjectprovider.exe
\windows\system32\deviceeject.exe
\windows\system32\devicepairingwizard.exe
\windows\system32\deviceproperties.exe
\windows\system32\dfdwiz.exe
\windows\system32\dfrgfat.exe
\windows\system32\dfrgifc.exe
\windows\system32\dfrgntfs.exe
\windows\system32\dfrgui.exe
\windows\system32\dfsr.exe
\windows\system32\dialer.exe
\windows\system32\diantz.exe
\windows\system32\dinotify.exe
\windows\system32\diskpart.exe
\windows\system32\diskperf.exe
\windows\system32\diskraid.exe
\windows\system32\dism.exe
\windows\system32\dism\dismhost.exe
\windows\system32\dispdiag.exe
\windows\system32\displayswitch.exe
\windows\system32\djoin.exe
\windows\system32\dllcache\accwiz.exe
\windows\system32\dllcache\actmovie.exe
\windows\system32\dllcache\admin.exe
\windows\system32\dllcache\agentsvr.exe
\windows\system32\dllcache\ahui.exe
\windows\system32\dllcache\alg.exe
\windows\system32\dllcache\append.exe
\windows\system32\dllcache\arp.exe
\windows\system32\dllcache\asr_fmt.exe
\windows\system32\dllcache\asr_ldm.exe
\windows\system32\dllcache\asr_pfu.exe
\windows\system32\dllcache\at.exe
\windows\system32\dllcache\atmadm.exe
\windows\system32\dllcache\attrib.exe
\windows\system32\dllcache\auditusr.exe
\windows\system32\dllcache\author.exe
\windows\system32\dllcache\autochk.exe
\windows\system32\dllcache\autoconv.exe
\windows\system32\dllcache\autofmt.exe
\windows\system32\dllcache\autolfn.exe
\windows\system32\dllcache\bckgzm.exe
\windows\system32\dllcache\blastcln.exe
\windows\system32\dllcache\bootcfg.exe
\windows\system32\dllcache\bootok.exe
\windows\system32\dllcache\bootvrfy.exe
\windows\system32\dllcache\cacls.exe
\windows\system32\dllcache\calc.exe
\windows\system32\dllcache\cb32.exe
\windows\system32\dllcache\cfgwiz.exe
\windows\system32\dllcache\change.exe
\windows\system32\dllcache\charmap.exe
\windows\system32\dllcache\chglogon.exe
\windows\system32\dllcache\chgport.exe
\windows\system32\dllcache\chgusr.exe
\windows\system32\dllcache\chkdsk.exe
\windows\system32\dllcache\chkntfs.exe
\windows\system32\dllcache\chkrzm.exe
\windows\system32\dllcache\cidaemon.exe
\windows\system32\dllcache\cintsetp.exe
\windows\system32\dllcache\cipher.exe
\windows\system32\dllcache\cisvc.exe
\windows\system32\dllcache\ckcnv.exe
\windows\system32\dllcache\cleanmgr.exe
\windows\system32\dllcache\clipbrd.exe
\windows\system32\dllcache\clipsrv.exe
\windows\system32\dllcache\cmd.exe
\windows\system32\dllcache\cmdl32.exe
\windows\system32\dllcache\cmmon32.exe
\windows\system32\dllcache\cmstp.exe
\windows\system32\dllcache\comp.exe
\windows\system32\dllcache\compact.exe
\windows\system32\dllcache\comrepl.exe
\windows\system32\dllcache\comrereg.exe
\windows\system32\dllcache\conf.exe
\windows\system32\dllcache\conime.exe
\windows\system32\dllcache\control.exe
\windows\system32\dllcache\convert.exe
\windows\system32\dllcache\convlog.exe
\windows\system32\dllcache\cplexe.exe
\windows\system32\dllcache\cprofile.exe
\windows\system32\dllcache\cscript.exe
\windows\system32\dllcache\csrss.exe
\windows\system32\dllcache\ctfmon.exe
\windows\system32\dllcache\davcdata.exe
\windows\system32\dllcache\dcomcnfg.exe
\windows\system32\dllcache\ddeshare.exe
\windows\system32\dllcache\debug.exe
\windows\system32\dllcache\defrag.exe
\windows\system32\dllcache\dfrgfat.exe
\windows\system32\dllcache\dfrgntfs.exe
\windows\system32\dllcache\dialer.exe
\windows\system32\dllcache\diantz.exe
\windows\system32\dllcache\diskpart.exe
\windows\system32\dllcache\diskperf.exe
\windows\system32\dllcache\dllhost.exe
\windows\system32\dllcache\dllhst3g.exe
\windows\system32\dllcache\dmadmin.exe
\windows\system32\dllcache\dmremote.exe
\windows\system32\dllcache\doskey.exe
\windows\system32\dllcache\dosx.exe
\windows\system32\dllcache\dplaysvr.exe
\windows\system32\dllcache\dpnsvr.exe
\windows\system32\dllcache\dpvsetup.exe
\windows\system32\dllcache\drvqry.exe
\windows\system32\dllcache\drwatson.exe
\windows\system32\dllcache\drwtsn32.exe
\windows\system32\dllcache\dumprep.exe
\windows\system32\dllcache\dvdupgrd.exe
\windows\system32\dllcache\dwwin.exe
\windows\system32\dllcache\dxdiag.exe
\windows\system32\dllcache\edlin.exe
\windows\system32\dllcache\esentutl.exe
\windows\system32\dllcache\eudcedit.exe
\windows\system32\dllcache\evcreate.exe
\windows\system32\dllcache\eventvwr.exe
\windows\system32\dllcache\evntcmd.exe
\windows\system32\dllcache\evntwin.exe
\windows\system32\dllcache\evtrig.exe
\windows\system32\dllcache\exch_regtrace.exe
\windows\system32\dllcache\exe2bin.exe
\windows\system32\dllcache\expand.exe
\windows\system32\dllcache\explorer.exe
\windows\system32\dllcache\extrac32.exe
\windows\system32\dllcache\fastopen.exe
\windows\system32\dllcache\fc.exe
\windows\system32\dllcache\find.exe
\windows\system32\dllcache\findstr.exe
\windows\system32\dllcache\finger.exe
\windows\system32\dllcache\fixmapi.exe
\windows\system32\dllcache\flattemp.exe
\windows\system32\dllcache\fltmc.exe
\windows\system32\dllcache\fontview.exe
\windows\system32\dllcache\forcedos.exe
\windows\system32\dllcache\fp98sadm.exe
\windows\system32\dllcache\fp98swin.exe
\windows\system32\dllcache\fpadmcgi.exe
\windows\system32\dllcache\fpcount.exe
\windows\system32\dllcache\fpremadm.exe
\windows\system32\dllcache\freecell.exe
\windows\system32\dllcache\fsutil.exe
\windows\system32\dllcache\ftp.exe
\windows\system32\dllcache\fxsclnt.exe
\windows\system32\dllcache\fxscover.exe
\windows\system32\dllcache\fxssend.exe
\windows\system32\dllcache\fxssvc.exe
\windows\system32\dllcache\gdi.exe
\windows\system32\dllcache\getmac.exe
\windows\system32\dllcache\gprslt.exe
\windows\system32\dllcache\gpupdate.exe
\windows\system32\dllcache\grpconv.exe
\windows\system32\dllcache\help.exe
\windows\system32\dllcache\helpctr.exe
\windows\system32\dllcache\helphost.exe
\windows\system32\dllcache\helpsvc.exe
\windows\system32\dllcache\hh.exe
\windows\system32\dllcache\hostname.exe
\windows\system32\dllcache\hrtzzm.exe
\windows\system32\dllcache\hscupd.exe
\windows\system32\dllcache\icwconn1.exe
\windows\system32\dllcache\icwconn2.exe
\windows\system32\dllcache\icwrmind.exe
\windows\system32\dllcache\icwtutor.exe
\windows\system32\dllcache\ie4uinit.exe
\windows\system32\dllcache\iedw.exe
\windows\system32\dllcache\iexplore.exe
\windows\system32\dllcache\iexpress.exe
\windows\system32\dllcache\iisreset.exe
\windows\system32\dllcache\iisrstas.exe
\windows\system32\dllcache\iissync.exe
\windows\system32\dllcache\imapi.exe
\windows\system32\dllcache\imekrmig.exe
\windows\system32\dllcache\imepadsv.exe
\windows\system32\dllcache\imjpdadm.exe
\windows\system32\dllcache\imjpdct.exe
\windows\system32\dllcache\imjpdsvr.exe
\windows\system32\dllcache\imjpinst.exe
\windows\system32\dllcache\imjpmig.exe
\windows\system32\dllcache\imjprw.exe
\windows\system32\dllcache\imjpuex.exe
\windows\system32\dllcache\imjputy.exe
\windows\system32\dllcache\imkrinst.exe
\windows\system32\dllcache\imscinst.exe
\windows\system32\dllcache\inetin51.exe
\windows\system32\dllcache\inetmgr.exe
\windows\system32\dllcache\inetwiz.exe
\windows\system32\dllcache\ipconfig.exe
\windows\system32\dllcache\ipsec6.exe
\windows\system32\dllcache\ipv6.exe
\windows\system32\dllcache\ipxroute.exe
\windows\system32\dllcache\isignup.exe
\windows\system32\dllcache\krnl386.exe
\windows\system32\dllcache\label.exe
\windows\system32\dllcache\lhmstsc.exe
\windows\system32\dllcache\lights.exe
\windows\system32\dllcache\lnkstub.exe
\windows\system32\dllcache\locator.exe
\windows\system32\dllcache\lodctr.exe
\windows\system32\dllcache\logagent.exe
\windows\system32\dllcache\logman.exe
\windows\system32\dllcache\logoff.exe
\windows\system32\dllcache\logonui.exe
\windows\system32\dllcache\lpq.exe
\windows\system32\dllcache\lpr.exe
\windows\system32\dllcache\lsass.exe
\windows\system32\dllcache\magnify.exe
\windows\system32\dllcache\makecab.exe
\windows\system32\dllcache\mem.exe
\windows\system32\dllcache\migisol.exe
\windows\system32\dllcache\migload.exe
\windows\system32\dllcache\migrate.exe
\windows\system32\dllcache\migregdb.exe
\windows\system32\dllcache\migwiz.exe
\windows\system32\dllcache\migwiza.exe
\windows\system32\dllcache\mmc.exe
\windows\system32\dllcache\mmcperf.exe
\windows\system32\dllcache\mnmsrvc.exe
\windows\system32\dllcache\mobsync.exe
\windows\system32\dllcache\mofcomp.exe
\windows\system32\dllcache\mountvol.exe
\windows\system32\dllcache\moviemk.exe
\windows\system32\dllcache\mplay32.exe
\windows\system32\dllcache\mplayer2.exe
\windows\system32\dllcache\mpnotify.exe
\windows\system32\dllcache\mqbkup.exe
\windows\system32\dllcache\mqsvc.exe
\windows\system32\dllcache\mqtgsvc.exe
\windows\system32\dllcache\mrinfo.exe
\windows\system32\dllcache\mscdexnt.exe
\windows\system32\dllcache\msconfig.exe
\windows\system32\dllcache\msdtc.exe
\windows\system32\dllcache\msg.exe
\windows\system32\dllcache\mshearts.exe
\windows\system32\dllcache\mshta.exe
\windows\system32\dllcache\msiexec.exe
\windows\system32\dllcache\msimn.exe
\windows\system32\dllcache\msinfo32.exe
\windows\system32\dllcache\msiregmv.exe
\windows\system32\dllcache\msoobe.exe
\windows\system32\dllcache\mspaint.exe
\windows\system32\dllcache\msswchx.exe
\windows\system32\dllcache\mstinit.exe
\windows\system32\dllcache\mtstocom.exe
\windows\system32\dllcache\muisetup.exe
\windows\system32\dllcache\napstat.exe
\windows\system32\dllcache\narrator.exe
\windows\system32\dllcache\nbtstat.exe
\windows\system32\dllcache\nddeapir.exe
\windows\system32\dllcache\net.exe
\windows\system32\dllcache\net1.exe
\windows\system32\dllcache\netdde.exe
\windows\system32\dllcache\netsetup.exe
\windows\system32\dllcache\netsh.exe
\windows\system32\dllcache\netstat.exe
\windows\system32\dllcache\nlsfunc.exe
\windows\system32\dllcache\notepad.exe
\windows\system32\dllcache\notiflag.exe
\windows\system32\dllcache\nppagent.exe
\windows\system32\dllcache\nslookup.exe
\windows\system32\dllcache\ntbackup.exe
\windows\system32\dllcache\ntsd.exe
\windows\system32\dllcache\ntvdm.exe
\windows\system32\dllcache\nw16.exe
\windows\system32\dllcache\nwscript.exe
\windows\system32\dllcache\odbcad32.exe
\windows\system32\dllcache\odbcconf.exe
\windows\system32\dllcache\oemig50.exe
\windows\system32\dllcache\oobebaln.exe
\windows\system32\dllcache\opnfiles.exe
\windows\system32\dllcache\osk.exe
\windows\system32\dllcache\osuninst.exe
\windows\system32\dllcache\packager.exe
\windows\system32\dllcache\pathping.exe
\windows\system32\dllcache\pentnt.exe
\windows\system32\dllcache\perfmon.exe
\windows\system32\dllcache\pinball.exe
\windows\system32\dllcache\ping.exe
\windows\system32\dllcache\ping6.exe
\windows\system32\dllcache\pintlphr.exe
\windows\system32\dllcache\powercfg.exe
\windows\system32\dllcache\print.exe
\windows\system32\dllcache\progman.exe
\windows\system32\dllcache\proquota.exe
\windows\system32\dllcache\proxycfg.exe
\windows\system32\dllcache\qappsrv.exe
\windows\system32\dllcache\qprocess.exe
\windows\system32\dllcache\query.exe
\windows\system32\dllcache\quser.exe
\windows\system32\dllcache\qwinsta.exe
\windows\system32\dllcache\rasautou.exe
\windows\system32\dllcache\rasdial.exe
\windows\system32\dllcache\rasphone.exe
\windows\system32\dllcache\rcimlby.exe
\windows\system32\dllcache\rcp.exe
\windows\system32\dllcache\rdpclip.exe
\windows\system32\dllcache\rdsaddin.exe
\windows\system32\dllcache\rdshost.exe
\windows\system32\dllcache\recover.exe
\windows\system32\dllcache\redir.exe
\windows\system32\dllcache\reg.exe
\windows\system32\dllcache\regedit.exe
\windows\system32\dllcache\regedt32.exe
\windows\system32\dllcache\regini.exe
\windows\system32\dllcache\register.exe
\windows\system32\dllcache\regsvr32.exe
\windows\system32\dllcache\regwiz.exe
\windows\system32\dllcache\relog.exe
\windows\system32\dllcache\replace.exe
\windows\system32\dllcache\reset.exe
\windows\system32\dllcache\rexec.exe
\windows\system32\dllcache\route.exe
\windows\system32\dllcache\routemon.exe
\windows\system32\dllcache\rsh.exe
\windows\system32\dllcache\rsm.exe
\windows\system32\dllcache\rsmsink.exe
\windows\system32\dllcache\rsmui.exe
\windows\system32\dllcache\rsnotify.exe
\windows\system32\dllcache\rsopprov.exe
\windows\system32\dllcache\rstrui.exe
\windows\system32\dllcache\rsvp.exe
\windows\system32\dllcache\rtcshare.exe
\windows\system32\dllcache\runas.exe
\windows\system32\dllcache\rundll32.exe
\windows\system32\dllcache\runonce.exe
\windows\system32\dllcache\rvsezm.exe
\windows\system32\dllcache\rwinsta.exe
\windows\system32\dllcache\sapisvr.exe
\windows\system32\dllcache\savedump.exe
\windows\system32\dllcache\sc.exe
\windows\system32\dllcache\scardsvr.exe
\windows\system32\dllcache\scrcons.exe
\windows\system32\dllcache\sctasks.exe
\windows\system32\dllcache\sdbinst.exe
\windows\system32\dllcache\secedit.exe
\windows\system32\dllcache\services.exe
\windows\system32\dllcache\sessmgr.exe
\windows\system32\dllcache\sethc.exe
\windows\system32\dllcache\setup.exe
\windows\system32\dllcache\setup50.exe
\windows\system32\dllcache\setup_wm.exe
\windows\system32\dllcache\setupn.exe
\windows\system32\dllcache\sfc.exe
\windows\system32\dllcache\shadow.exe
\windows\system32\dllcache\share.exe
\windows\system32\dllcache\shmgrate.exe
\windows\system32\dllcache\shrpubw.exe
\windows\system32\dllcache\shtml.exe
\windows\system32\dllcache\shutdown.exe
\windows\system32\dllcache\shvlzm.exe
\windows\system32\dllcache\sigverif.exe
\windows\system32\dllcache\skeys.exe
\windows\system32\dllcache\smbinst.exe
\windows\system32\dllcache\smi2smir.exe
\windows\system32\dllcache\smlogsvc.exe
\windows\system32\dllcache\smss.exe
\windows\system32\dllcache\sndrec32.exe
\windows\system32\dllcache\sndvol32.exe
\windows\system32\dllcache\snmp.exe
\windows\system32\dllcache\snmptrap.exe
\windows\system32\dllcache\sol.exe
\windows\system32\dllcache\sort.exe
\windows\system32\dllcache\spider.exe
\windows\system32\dllcache\spiisupd.exe
\windows\system32\dllcache\spnpinst.exe
\windows\system32\dllcache\spoolsv.exe
\windows\system32\dllcache\sprestrt.exe
\windows\system32\dllcache\srdiag.exe
\windows\system32\dllcache\stimon.exe
\windows\system32\dllcache\subst.exe
\windows\system32\dllcache\svchost.exe
\windows\system32\dllcache\syncapp.exe
\windows\system32\dllcache\sysedit.exe
\windows\system32\dllcache\sysinfo.exe
\windows\system32\dllcache\syskey.exe
\windows\system32\dllcache\sysocmgr.exe
\windows\system32\dllcache\systray.exe
\windows\system32\dllcache\taskkill.exe
\windows\system32\dllcache\tasklist.exe
\windows\system32\dllcache\taskman.exe
\windows\system32\dllcache\taskmgr.exe
\windows\system32\dllcache\tcmsetup.exe
\windows\system32\dllcache\tcpsvcs.exe
\windows\system32\dllcache\tcptest.exe
\windows\system32\dllcache\telnet.exe
\windows\system32\dllcache\tftp.exe
\windows\system32\dllcache\tintlphr.exe
\windows\system32\dllcache\tintsetp.exe
\windows\system32\dllcache\tlntadmn.exe
\windows\system32\dllcache\tlntsess.exe
\windows\system32\dllcache\tlntsvr.exe
\windows\system32\dllcache\tourstrt.exe
\windows\system32\dllcache\tourw.exe
\windows\system32\dllcache\tracerpt.exe
\windows\system32\dllcache\tracert.exe
\windows\system32\dllcache\tracert6.exe
\windows\system32\dllcache\tscon.exe
\windows\system32\dllcache\tsdiscon.exe
\windows\system32\dllcache\tskill.exe
\windows\system32\dllcache\tsprof.exe
\windows\system32\dllcache\tsshutdn.exe
\windows\system32\dllcache\twunk_16.exe
\windows\system32\dllcache\twunk_32.exe
\windows\system32\dllcache\typeperf.exe
\windows\system32\dllcache\unlodctr.exe
\windows\system32\dllcache\unregmp2.exe
\windows\system32\dllcache\unsecapp.exe
\windows\system32\dllcache\uploadm.exe
\windows\system32\dllcache\upnpcont.exe
\windows\system32\dllcache\ups.exe
\windows\system32\dllcache\user.exe
\windows\system32\dllcache\userinit.exe
\windows\system32\dllcache\utilman.exe
\windows\system32\dllcache\verifier.exe
\windows\system32\dllcache\vssadmin.exe
\windows\system32\dllcache\vssvc.exe
\windows\system32\dllcache\vwipxspx.exe
\windows\system32\dllcache\w32tm.exe
\windows\system32\dllcache\wab.exe
\windows\system32\dllcache\wabmig.exe
\windows\system32\dllcache\wb32.exe
\windows\system32\dllcache\wbemtest.exe
\windows\system32\dllcache\wextract.exe
\windows\system32\dllcache\wiaacmgr.exe
\windows\system32\dllcache\winchat.exe
\windows\system32\dllcache\winhelp.exe
\windows\system32\dllcache\winhlp32.exe
\windows\system32\dllcache\winhstb.exe
\windows\system32\dllcache\winlogon.exe
\windows\system32\dllcache\winmgmt.exe
\windows\system32\dllcache\winmine.exe
\windows\system32\dllcache\winmsd.exe
\windows\system32\dllcache\winspool.exe
\windows\system32\dllcache\winver.exe
\windows\system32\dllcache\wmiadap.exe
\windows\system32\dllcache\wmiapsrv.exe
\windows\system32\dllcache\wmic.exe
\windows\system32\dllcache\wmiprvse.exe
\windows\system32\dllcache\wmplayer.exe
\windows\system32\dllcache\wordpad.exe
\windows\system32\dllcache\wowdeb.exe
\windows\system32\dllcache\wowexec.exe
\windows\system32\dllcache\wpabaln.exe
\windows\system32\dllcache\wpnpinst.exe
\windows\system32\dllcache\write.exe
\windows\system32\dllcache\wscntfy.exe
\windows\system32\dllcache\wscript.exe
\windows\system32\dllcache\wuauclt.exe
\windows\system32\dllcache\wuauclt1.exe
\windows\system32\dllcache\wupdmgr.exe
\windows\system32\dllcache\xcopy.exe
\windows\system32\dllcache\zclientm.exe
\windows\system32\dllhost.exe
\windows\system32\dllhst3g.exe
\windows\system32\dmadmin.exe
\windows\system32\dmremote.exe
\windows\system32\dnscacheugc.exe
\windows\system32\doskey.exe
\windows\system32\dosx.exe
\windows\system32\dpapimig.exe
\windows\system32\dpiscaling.exe
\windows\system32\dplaysvr.exe
\windows\system32\dpnsvr.exe
\windows\system32\dpvsetup.exe
\windows\system32\driverquery.exe
\windows\system32\drvinst.exe
\windows\system32\drwatson.exe
\windows\system32\drwtsn32.exe
\windows\system32\dumprep.exe
\windows\system32\dvdplay.exe
\windows\system32\dvdupgrd.exe
\windows\system32\dwm.exe
\windows\system32\dwwin.exe
\windows\system32\dxdiag.exe
\windows\system32\dxpserver.exe
\windows\system32\eap3host.exe
\windows\system32\edlin.exe
\windows\system32\efsui.exe
\windows\system32\ehstorauthn.exe
\windows\system32\esentutl.exe
\windows\system32\eudcedit.exe
\windows\system32\eventcreate.exe
\windows\system32\eventtriggers.exe
\windows\system32\eventvwr.exe
\windows\system32\exe2bin.exe
\windows\system32\expand.exe
\windows\system32\extrac32.exe
\windows\system32\fastopen.exe
\windows\system32\fc.exe
\windows\system32\find.exe
\windows\system32\findstr.exe
\windows\system32\finger.exe
\windows\system32\firewallcontrolpanel.exe
\windows\system32\firewallsettings.exe
\windows\system32\fixmapi.exe
\windows\system32\fltmc.exe
\windows\system32\fontview.exe
\windows\system32\forcedos.exe
\windows\system32\forfiles.exe
\windows\system32\freecell.exe
\windows\system32\fsquirt.exe
\windows\system32\fsutil.exe
\windows\system32\ftp.exe
\windows\system32\fvenotify.exe
\windows\system32\fveprompt.exe
\windows\system32\fxscover.exe
\windows\system32\fxssvc.exe
\windows\system32\fxsunatd.exe
\windows\system32\gdi.exe
\windows\system32\getmac.exe
\windows\system32\gettingstarted.exe
\windows\system32\gpresult.exe
\windows\system32\gpscript.exe
\windows\system32\gpupdate.exe
\windows\system32\grpconv.exe
\windows\system32\hdwwiz.exe
\windows\system32\help.exe
\windows\system32\hostname.exe
\windows\system32\hwrcomp.exe
\windows\system32\hwrreg.exe
\windows\system32\iashost.exe
\windows\system32\icacls.exe
\windows\system32\icardagt.exe
\windows\system32\icsunattend.exe
\windows\system32\ie4uinit.exe
\windows\system32\ieunatt.exe
\windows\system32\iexpress.exe
\windows\system32\imapi.exe
\windows\system32\ime\imejp10\imjpdadm.exe
\windows\system32\ime\imejp10\imjpdct.exe
\windows\system32\ime\imejp10\imjpdsvr.exe
\windows\system32\ime\imejp10\imjpmgr.exe
\windows\system32\ime\imejp10\imjppdmg.exe
\windows\system32\ime\imejp10\imjpuex.exe
\windows\system32\ime\imejp10\imjpuexc.exe
\windows\system32\ime\imesc5\imscprop.exe
\windows\system32\ime\imetc10\imtcprop.exe
\windows\system32\ime\shared\imccphr.exe
\windows\system32\ime\shared\imepadsv.exe
\windows\system32\infdefaultinstall.exe
\windows\system32\ipconfig.exe
\windows\system32\ipsec6.exe
\windows\system32\ipv6.exe
\windows\system32\ipxroute.exe
\windows\system32\irftp.exe
\windows\system32\iscsicli.exe
\windows\system32\iscsicpl.exe
\windows\system32\isoburn.exe
\windows\system32\klist.exe
\windows\system32\krnl386.exe
\windows\system32\ksetup.exe
\windows\system32\ktmutil.exe
\windows\system32\label.exe
\windows\system32\lights.exe
\windows\system32\lnkstub.exe
\windows\system32\locationnotifications.exe
\windows\system32\locator.exe
\windows\system32\lodctr.exe
\windows\system32\logagent.exe
\windows\system32\logman.exe
\windows\system32\logoff.exe
\windows\system32\logonui.exe
\windows\system32\lpksetup.exe
\windows\system32\lpq.exe
\windows\system32\lpr.exe
\windows\system32\lpremove.exe
\windows\system32\lsass.exe
\windows\system32\lsm.exe
\windows\system32\magnify.exe
\windows\system32\makecab.exe
\windows\system32\manage-bde.exe
\windows\system32\mblctr.exe
\windows\system32\mcbuilder.exe
\windows\system32\mctadmin.exe
\windows\system32\mdres.exe
\windows\system32\mdsched.exe
\windows\system32\mem.exe
\windows\system32\mfpmp.exe
\windows\system32\migautoplay.exe
\windows\system32\migpwd.exe
\windows\system32\migwiz\mighost.exe
\windows\system32\migwiz\migsetup.exe
\windows\system32\migwiz\migwiz.exe
\windows\system32\migwiz\postmig.exe
\windows\system32\mmc.exe
\windows\system32\mmcperf.exe
\windows\system32\mnmsrvc.exe
\windows\system32\mobsync.exe
\windows\system32\mountvol.exe
\windows\system32\mplay32.exe
\windows\system32\mpnotify.exe
\windows\system32\mqbkup.exe
\windows\system32\mqsvc.exe
\windows\system32\mqtgsvc.exe
\windows\system32\mrinfo.exe
\windows\system32\mrt.exe
\windows\system32\mscdexnt.exe
\windows\system32\msconfig.exe
\windows\system32\msdt.exe
\windows\system32\msdtc.exe
\windows\system32\msfeedssync.exe
\windows\system32\msg.exe
\windows\system32\mshearts.exe
\windows\system32\mshta.exe
\windows\system32\msiexec.exe
\windows\system32\msinfo32.exe
\windows\system32\mspaint.exe
\windows\system32\msra.exe
\windows\system32\msswchx.exe
\windows\system32\mstinit.exe
\windows\system32\mstsc.exe
\windows\system32\mtstocom.exe
\windows\system32\muiunattend.exe
\windows\system32\multidigimon.exe
\windows\system32\napstat.exe
\windows\system32\narrator.exe
\windows\system32\nbtstat.exe
\windows\system32\ndadmin.exe
\windows\system32\nddeapir.exe
\windows\system32\net.exe
\windows\system32\net1.exe
\windows\system32\netbtugc.exe
\windows\system32\netcfg.exe
\windows\system32\netdde.exe
\windows\system32\netiougc.exe
\windows\system32\netplwiz.exe
\windows\system32\netproj.exe
\windows\system32\netsetup.exe
\windows\system32\netsh.exe
\windows\system32\netstat.exe
\windows\system32\newdev.exe
\windows\system32\nlsfunc.exe
\windows\system32\nltest.exe
\windows\system32\notepad.exe
\windows\system32\npp\nppagent.exe
\windows\system32\nslookup.exe
\windows\system32\ntbackup.exe
\windows\system32\ntkrnlpa.exe
\windows\system32\ntoskrnl.exe
\windows\system32\ntprint.exe
\windows\system32\ntsd.exe
\windows\system32\ntvdm.exe
\windows\system32\nw16.exe
\windows\system32\nwscript.exe
\windows\system32\ocsetup.exe
\windows\system32\odbcad32.exe
\windows\system32\odbcconf.exe
\windows\system32\oobe\audit.exe
\windows\system32\oobe\msoobe.exe
\windows\system32\oobe\oobebaln.exe
\windows\system32\oobe\oobeldr.exe
\windows\system32\oobe\setup.exe
\windows\system32\oobe\setupsqm.exe
\windows\system32\oobe\windeploy.exe
\windows\system32\openfiles.exe
\windows\system32\optionalfeatures.exe
\windows\system32\osk.exe
\windows\system32\osuninst.exe
\windows\system32\p2phost.exe
\windows\system32\packager.exe
\windows\system32\pathping.exe
\windows\system32\pcaelv.exe
\windows\system32\pcalua.exe
\windows\system32\pcaui.exe
\windows\system32\pcawrk.exe
\windows\system32\pcwrun.exe
\windows\system32\pentnt.exe
\windows\system32\perfmon.exe
\windows\system32\ping.exe
\windows\system32\ping6.exe
\windows\system32\pkgmgr.exe
\windows\system32\plasrv.exe
\windows\system32\pnpunattend.exe
\windows\system32\pnputil.exe
\windows\system32\poqexec.exe
\windows\system32\powercfg.exe
\windows\system32\presentationhost.exe
\windows\system32\presentationsettings.exe
\windows\system32\prevhost.exe
\windows\system32\print.exe
\windows\system32\printbrmui.exe
\windows\system32\printfilterpipelinesvc.exe
\windows\system32\printisolationhost.exe
\windows\system32\printui.exe
\windows\system32\progman.exe
\windows\system32\proquota.exe
\windows\system32\proxycfg.exe
\windows\system32\psr.exe
\windows\system32\pushprinterconnections.exe
\windows\system32\qappsrv.exe
\windows\system32\qprocess.exe
\windows\system32\query.exe
\windows\system32\quser.exe
\windows\system32\qwinsta.exe
\windows\system32\racagent.exe
\windows\system32\rasautou.exe
\windows\system32\rasdial.exe
\windows\system32\raserver.exe
\windows\system32\rasphone.exe
\windows\system32\rcimlby.exe
\windows\system32\rcp.exe
\windows\system32\rdpclip.exe
\windows\system32\rdpinit.exe
\windows\system32\rdpshell.exe
\windows\system32\rdpsign.exe
\windows\system32\rdrleakdiag.exe
\windows\system32\rdsaddin.exe
\windows\system32\rdshost.exe
\windows\system32\reagentc.exe
\windows\system32\recdisc.exe
\windows\system32\recover.exe
\windows\system32\redir.exe
\windows\system32\reg.exe
\windows\system32\regedt32.exe
\windows\system32\regini.exe
\windows\system32\registeriepkeys.exe
\windows\system32\regsvr32.exe
\windows\system32\regwiz.exe
\windows\system32\rekeywiz.exe
\windows\system32\relog.exe
\windows\system32\relpost.exe
\windows\system32\repair-bde.exe
\windows\system32\replace.exe
\windows\system32\reset.exe
\windows\system32\resmon.exe
\windows\system32\restore\rstrui.exe
\windows\system32\restore\srdiag.exe
\windows\system32\rexec.exe
\windows\system32\rmactivate.exe
\windows\system32\rmactivate_isv.exe
\windows\system32\rmactivate_ssp.exe
\windows\system32\rmactivate_ssp_isv.exe
\windows\system32\rmclient.exe
\windows\system32\robocopy.exe
\windows\system32\route.exe
\windows\system32\routemon.exe
\windows\system32\rpcping.exe
\windows\system32\rrinstaller.exe
\windows\system32\rsh.exe
\windows\system32\rsm.exe
\windows\system32\rsmsink.exe
\windows\system32\rsmui.exe
\windows\system32\rsnotify.exe
\windows\system32\rsopprov.exe
\windows\system32\rstrui.exe
\windows\system32\rsvp.exe
\windows\system32\rtcshare.exe
\windows\system32\runas.exe
\windows\system32\rundll32.exe
\windows\system32\runlegacycplelevated.exe
\windows\system32\runonce.exe
\windows\system32\rwinsta.exe
\windows\system32\savedump.exe
\windows\system32\sbunattend.exe
\windows\system32\sc.exe
\windows\system32\scardsvr.exe
\windows\system32\schtasks.exe
\windows\system32\sdbinst.exe
\windows\system32\sdchange.exe
\windows\system32\sdclt.exe
\windows\system32\sdiagnhost.exe
\windows\system32\searchfilterhost.exe
\windows\system32\searchindexer.exe
\windows\system32\searchprotocolhost.exe
\windows\system32\secedit.exe
\windows\system32\secinit.exe
\windows\system32\services.exe
\windows\system32\sessmgr.exe
\windows\system32\sethc.exe
\windows\system32\setieinstalleddate.exe
\windows\system32\setspn.exe
\windows\system32\setup.exe
\windows\system32\setupcl.exe
\windows\system32\setupn.exe
\windows\system32\setupsnk.exe
\windows\system32\setupugc.exe
\windows\system32\setver.exe
\windows\system32\setx.exe
\windows\system32\sfc.exe
\windows\system32\shadow.exe
\windows\system32\share.exe
\windows\system32\shmgrate.exe
\windows\system32\shrpubw.exe
\windows\system32\shutdown.exe
\windows\system32\sigverif.exe
\windows\system32\skeys.exe
\windows\system32\sllua.exe
\windows\system32\slsvc.exe
\windows\system32\slui.exe
\windows\system32\smbinst.exe
\windows\system32\smlogsvc.exe
\windows\system32\smss.exe
\windows\system32\sndrec32.exe
\windows\system32\sndvol.exe
\windows\system32\sndvol32.exe
\windows\system32\snippingtool.exe
\windows\system32\snmptrap.exe
\windows\system32\sol.exe
\windows\system32\sort.exe
\windows\system32\soundrecorder.exe
\windows\system32\speech\speechux\speechuxtutorial.exe
\windows\system32\speech\speechux\speechuxwiz.exe
\windows\system32\spider.exe
\windows\system32\spiisupd.exe
\windows\system32\spinstall.exe
\windows\system32\spnpinst.exe
\windows\system32\spool\tools\printbrm.exe
\windows\system32\spool\tools\printbrmengine.exe
\windows\system32\spoolsv.exe
\windows\system32\sppsvc.exe
\windows\system32\sprestrt.exe
\windows\system32\spreview.exe
\windows\system32\srdelayed.exe
\windows\system32\stikynot.exe
\windows\system32\stimon.exe
\windows\system32\subst.exe
\windows\system32\svchost.exe
\windows\system32\sxstrace.exe
\windows\system32\syncapp.exe
\windows\system32\synchost.exe
\windows\system32\sysedit.exe
\windows\system32\syskey.exe
\windows\system32\sysocmgr.exe
\windows\system32\sysprep\sysprep.exe
\windows\system32\systeminfo.exe
\windows\system32\systempropertiesadvanced.exe
\windows\system32\systempropertiescomputername.exe
\windows\system32\systempropertiesdataexecutionprevention.exe
\windows\system32\systempropertieshardware.exe
\windows\system32\systempropertiesperformance.exe
\windows\system32\systempropertiesprotection.exe
\windows\system32\systempropertiesremote.exe
\windows\system32\systray.exe
\windows\system32\tabcal.exe
\windows\system32\takeown.exe
\windows\system32\tapiunattend.exe
\windows\system32\taskeng.exe
\windows\system32\taskhost.exe
\windows\system32\taskkill.exe
\windows\system32\tasklist.exe
\windows\system32\taskman.exe
\windows\system32\taskmgr.exe
\windows\system32\tcmsetup.exe
\windows\system32\tcpsvcs.exe
\windows\system32\telnet.exe
\windows\system32\tftp.exe
\windows\system32\timeout.exe
\windows\system32\tlntadmn.exe
\windows\system32\tlntsess.exe
\windows\system32\tlntsvr.exe
\windows\system32\tourstart.exe
\windows\system32\tpminit.exe
\windows\system32\tracerpt.exe
\windows\system32\tracert.exe
\windows\system32\tracert6.exe
\windows\system32\tscon.exe
\windows\system32\tscupgrd.exe
\windows\system32\tsdiscon.exe
\windows\system32\tskill.exe
\windows\system32\tsshutdn.exe
\windows\system32\tstheme.exe
\windows\system32\tswbprxy.exe
\windows\system32\tswpfwrp.exe
\windows\system32\typeperf.exe
\windows\system32\tzchange.exe
\windows\system32\tzutil.exe
\windows\system32\ucsvc.exe
\windows\system32\ui0detect.exe
\windows\system32\unattendedjoin.exe
\windows\system32\unlodctr.exe
\windows\system32\unregmp2.exe
\windows\system32\upnpcont.exe
\windows\system32\ups.exe
\windows\system32\user.exe
\windows\system32\useraccountcontrolsettings.exe
\windows\system32\userinit.exe
\windows\system32\usmt\migload.exe
\windows\system32\usmt\migwiz.exe
\windows\system32\usmt\migwiza.exe
\windows\system32\usrmlnka.exe
\windows\system32\usrprbda.exe
\windows\system32\usrshuta.exe
\windows\system32\utilman.exe
\windows\system32\vaultcmd.exe
\windows\system32\vaultsysui.exe
\windows\system32\vds.exe
\windows\system32\vdsldr.exe
\windows\system32\verclsid.exe
\windows\system32\verifier.exe
\windows\system32\vmicsvc.exe
\windows\system32\vsp1cln.exe
\windows\system32\vssadmin.exe
\windows\system32\vssvc.exe
\windows\system32\vwipxspx.exe
\windows\system32\w32tm.exe
\windows\system32\waitfor.exe
\windows\system32\wbadmin.exe
\windows\system32\wbem\mofcomp.exe
\windows\system32\wbem\scrcons.exe
\windows\system32\wbem\unsecapp.exe
\windows\system32\wbem\wbemtest.exe
\windows\system32\wbem\winmgmt.exe
\windows\system32\wbem\wmiadap.exe
\windows\system32\wbem\wmiapsrv.exe
\windows\system32\wbem\wmic.exe
\windows\system32\wbem\wmiprvse.exe
\windows\system32\wbengine.exe
\windows\system32\wecutil.exe
\windows\system32\wercon.exe
\windows\system32\werfault.exe
\windows\system32\werfaultsecure.exe
\windows\system32\wermgr.exe
\windows\system32\wevtutil.exe
\windows\system32\wextract.exe
\windows\system32\wfs.exe
\windows\system32\where.exe
\windows\system32\whoami.exe
\windows\system32\wiaacmgr.exe
\windows\system32\wimserv.exe
\windows\system32\winchat.exe
\windows\system32\windowsanytimeupgraderesults.exe
\windows\system32\windowspowershell\v1.0\powershell.exe
\windows\system32\windowspowershell\v1.0\powershell_ise.exe
\windows\system32\winfxdocobj.exe
\windows\system32\winhlp32.exe
\windows\system32\wininit.exe
\windows\system32\winload.exe
\windows\system32\winlogon.exe
\windows\system32\winmine.exe
\windows\system32\winmsd.exe
\windows\system32\winresume.exe
\windows\system32\winrs.exe
\windows\system32\winrshost.exe
\windows\system32\winsat.exe
\windows\system32\winspool.exe
\windows\system32\winver.exe
\windows\system32\wisptis.exe
\windows\system32\wksprt.exe
\windows\system32\wlanext.exe
\windows\system32\wlrmdr.exe
\windows\system32\wowdeb.exe
\windows\system32\wowexec.exe
\windows\system32\wpabaln.exe
\windows\system32\wpcer.exe
\windows\system32\wpcumi.exe
\windows\system32\wpdshextautoplay.exe
\windows\system32\wpnpinst.exe
\windows\system32\write.exe
\windows\system32\wscntfy.exe
\windows\system32\wscript.exe
\windows\system32\wsmanhttpconfig.exe
\windows\system32\wsmprovhost.exe
\windows\system32\wsqmcons.exe
\windows\system32\wuapp.exe
\windows\system32\wuauclt.exe
\windows\system32\wuauclt1.exe
\windows\system32\wudfhost.exe
\windows\system32\wupdmgr.exe
\windows\system32\wusa.exe
\windows\system32\xcopy.exe
\windows\system32\xpsrchvw.exe
\windows\system32\xpsviewer\xpsviewer.exe
\windows\system32\xwizard.exe
\windows\taskman.exe
\windows\temp\rarsfx0\bootinst_w7ldr.exe
\windows\temp\rarsfx0\md5.exe
\windows\twunk_16.exe
\windows\twunk_32.exe
\windows\winhelp.exe
\windows\winhlp32.exe
\windows\write.exe
