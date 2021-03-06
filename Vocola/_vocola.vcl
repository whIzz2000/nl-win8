## Global voice commands

#  When overriding ensure commands have the same case and spelling
#  overrid in application-specific command files

include window_switching.vch;
include locals.vch;

### window and tab navigation

#Close Here                           = ButtonClick(2,1) Wait(100) c;
Close Prompt                         = {Alt+Space}c;
Context Menu                         = {shift+f10}; #{Alt+f}{Down};
# implemented elsewhere
#Close Window                        = {Alt+Space}c;
#Switch to Browser                   = AppBringUp(chrome);

(Switch|Next) View     = {Ctrl+Tab};
(Switch|Next) View <n> = {Ctrl+Tab_$2};
Previous View          = {Ctrl+Shift+Tab};
Previous View <n>      = {Ctrl+Shift+Tab_$1};

Back Tab      = {Shift+Tab};
Back Tab  <n> = {Shift+Tab_$1};
Page          = {PgDn};
Page <n>      = {PgDn_$1};
#Escape        = {Esc};

#accept application warning alert
okay alert = {tab}{enter};

# Open/Close a drop-down list
(Expand={Alt+ExtDown} | Collapse={Alt+ExtUp}) That = SendSystemKeys($1);

# ---------------------------------------------------------------------------
### Extension command mappings for Vocola

# use extension keyhold (Keys)
(hold|release) (shift|control=ctrl|tab|alternate=alt) button = Keys.SendInput({$2_$1});
# environment variable extension
type environment variable (home=HOME|path=PATH|unknown) = Env.Get($1,"UNKNOWN");
# insert date extension
Short date separator = "----{enter}" Date.Now("%d/%m/%y") "{enter}{enter}{enter}{up}";
# Windows clipboard extension
show clipboard = MsgBoxConfirm('"' Clipboard.Get() '"', 64,
                               "Current contents of clipboard");
set clipboard to <_anything> = Clipboard.Set($1);
# persistent variable extension
<v> := (first | second | third | fourth | fifth);
clipboard save [to] <v> register = Variable.Set($1, Clipboard.Get());
save clipboard [to] <v> register = Variable.Set($1, Clipboard.Get());
         set  <v> register 1..10 = Variable.Set  ($1, $2);
       unset  <v> register       = Variable.Unset($1);
         type <v> register       = Variable.Get($1, UNDEFINED);

# ---------------------------------------------------------------------------
### NatSpeak

#Dragon Menu              = SendSystemKeys( {NumKey*} );
#(Edit=v | Train=t) Words = SendSystemKeys( {NumKey*} ) Wait(100) w $1;
#Save Speech Files        = SendSystemKeys( {NumKey*} ) Wait(100) ff;
#Exit NatSpeak            = SendSystemKeys( {NumKey*} ) Wait(100) e;
#Die Die = GoToSleep();

#
# IE
##
#[search] Google for <_anything> = AppBringUp("IEXPLORE") {Alt+g}$1{Enter} ;

# ---------------------------------------------------------------------------
# Mouse Handling

#Hit Down         = ButtonClick();
#Hit Double       = ButtonClick(1,2);
(Shift           = 1 | Control                   = 2 | Alt = 3) Click = ShiftKey($1) ButtonClick();
#Hit Start [Menu] = SendSystemKeys( {Ctrl+Esc} );

## Straight mouse grid commands. (See documentation in utilities.vch)

include utilities.vch;
<n> := 0..30;

<n> <n> Go    = moveTo($2, $1);
<n> <n> Touch =  touch($2, $1);
<n> <n> Drag  = dragTo($2, $1);
#<n> <n> Paste =  touch($2, $1) {Ctrl+v};

<upDown>    := (  Up='-' |  Down='');
<leftRight> := (Left='-' | Right='');

Drag <n> <upDown>    = dragBy(0, $2$1);
Drag <n> <leftRight> = dragBy($2$1, 0);

# extension of mouse movement commands for greater range
<mouse_range_adjust> := (20|30|40|50|60|70|80|90);
# adjust pixel movement to seem more like the built-in "move mouse" grammars
Mouse <upDown> <mouse_range_adjust>    = moveBy(0, $1 Eval($2/5));
Mouse <leftRight> <mouse_range_adjust> = moveBy($1 Eval($2/5), 0);

### Move and resize windows
<ns> := 0..10;
Window move <direction> = SendSystemKeys({Win+$1});
Window move <direction> <ns> = Repeat($2, SendSystemKeys({Win+$1}));
Window maximise (swap | left | right) = SendSystemKeys({Win+Up})
    Repeat(2, SendSystemKeys({Win+Right})) SendSystemKeys({Win+Up});
#<edge> := (Top=n | Bottom=s | Left=w | Right=e);
#
#[Move] Window <n> <upDown>    = moveNearEdge(n,0,1) dragBy(0, $2$1);
#[Move] Window <n> <leftRight> = moveNearEdge(n,0,1) dragBy($2$1, 0);
#[Move] Window Northwest = moveNearEdge(nw,2,1) dragTo(2,1);
#[Move] Window Northeast = moveNearEdge(ne,-5,1) dragTo(95,1);
#
#[Size] Window <edge> <n> <upDown>    = moveToEdge($1) dragBy(0, $3$2);
#[Size] Window <edge> <n> <leftRight> = moveToEdge($1) dragBy($3$2, 0);
#
## implemented elsewhere
##Maximize Window = touchNearEdge(ne,-2,1);
#
#Tile Windows     = tileWindows(0);
#Tile Windows <n> = tileWindows($1);  # Edge is <n> units right of center

# ---------------------------------------------------------------------------
# Text Editing

<direction>  := Left | Right | Up | Down;
<left_right> := Left | Right;
<start_end> := (Start={Home} | End={End});
<compass> := (North={Shift+Ctrl+Home} | South={Shift+Ctrl+End} |
 East={Shift+End} | West={Shift+Home});

### Characters
# implemented elsewhere
#<n> <direction>       = {$2_$1};
Kill (Char | 1 | One) = {Del};
Kill Back [1]         = {Backspace};
Kill <n>              = {Del_$1};
[Kill] Back <n>       = {Backspace_$1};

### Words
[One] Word <left_right>= {Ctrl+$1};
<n> Words <left_right> = {Ctrl+$2_$1};
Kill Word              = {Right_2}{Ctrl+Left}{Shift+Ctrl+Right}   {Del};
Kill <n> Words         = {Right_2}{Ctrl+Left}{Shift+Ctrl+Right_$1}{Del};
Kill Back Word         = {Left}{Ctrl+Right}{Shift+Ctrl+Left}   {Del};
Kill Back <n> Words    = {Left}{Ctrl+Right}{Shift+Ctrl+Left_$1}{Del};

### Lines
Line <start_end>     = $1;
# implemented elsewhere
#New Line             = {Enter};
Line Here            = {Enter}{Left};
Copy Line            = {home}{Shift+End}{Ctrl+c};
Kill Line            = {home}{Shift+End}{Del};
Kill Back Line       = {home}{Shift+Up}  {Shift+Home}{Del};
Kill <n> Lines       = {home}{Shift+Down_$1}{Shift+Home}{Del};
Kill Back <n> Lines  = {home}{Shift+Up_$1}  {Shift+Home}{Del};
Kill Here            = {Shift+End}{Del};
Kill Back Here       = {Shift+Home}{Del};
Duplicate Line       = {home}{Shift+Down}{Shift+Home}{Ctrl+c}{Home}{Ctrl+v};
                    
### Paragraphs        
Graph Start          = {Ctrl+Up}{Right}{Home};
Graph End            = {Ctrl+Down}{Left_2}{End};
(Paragraph|Graph) Here = {Enter}{Enter}{Left}{Left};
Open (Graph|Line)    = {Enter}{Enter}{Left};
Copy Graph           = {Ctrl+Down}{Shift+Ctrl+Up}{Ctrl+c};
Kill Graph           = {Ctrl+Down}{Shift+Ctrl+Up}{Del};
Duplicate Graph      = {Ctrl+Down}{Shift+Ctrl+Up}{Ctrl+c}{Home}{Ctrl+v};
                    
### Entire "Flow"   
Flow Start           = {Ctrl+Home};
Flow End             = {Ctrl+End};
#New Line             = {Enter};
All           = {Ctrl+a};
Copy All             = {Ctrl+a}{Ctrl+c};
(Cut|Kill) All       = {Ctrl+a}{Ctrl+x};
Kill Flow Here       = {Ctrl+Shift+End} {Ctrl+x};
Kill Back Flow Here  = {Ctrl+Shift+Home}{Ctrl+x};
Replace All          = {Ctrl+a}{Del}{Ctrl+v};
                    
### Selection         
Kill That            = {Del};
# implemented elsewhere
#Cut That             = {Ctrl+x};
#Copy That            = {Ctrl+c};
Yank That            = {Ctrl+v};
Paste Here           = ButtonClick() {Ctrl+v};
Duplicate That       = {Ctrl+c}{Left}{Ctrl+v};
Keep That            = {Ctrl+c}{Ctrl+a}{Del}{Ctrl+v};
Select <compass>     = $1;

### Miscellaneous
undo that <n> = {Ctrl+z_$1};

include keys.vch;

# ---------------------------------------------------------------------------
#
# Tan custom commands
#

$set numbers 0;

## icon navigation commands Win 8

quickStartBar()   := Keys.SendInput({win+b});
(quick start bar|notification tray) = quickStartBar();

# open context menu for quick start icon given a row and column index (one based), weird quirk is that first column takes extra press to get the next row.
<lr> := (left={space}|right={shift+f10});
icon 1 1..4 <lr> = quickStartBar() Wait(100) Repeat( Eval('($1-1)'), Wait(50) {right}) $2;
icon 2..6 1..4 <lr> = quickStartBar() Wait(100) Repeat( Eval('(($1-1)*4)+($2)'), Wait(50) {right}) $3;

## Windows 8 shortcuts

open computer = SendSystemKeys({win+e});
search (programs=q|files=f|computer=s) = SendSystemKeys({win+$1});
open main menu = SendSystemKeys({win+x});
show all windows = SendSystemKeys({ctrl+alt+tab});
#(sound="{Down_4} Wait(200) {Right_1}"|network="{Down_4}") control = SendSystemKeys({Win+i}) $1; # {enter};
#win+i seems to work intermittently!
network control = SendSystemKeys({win+i}) {Down_4} {enter};

volumeControl() := SendSystemKeys({win+i}) {Down_4} Wait(100) {Right_1} {enter};
Volume control = volumeControl();
volume (up|down) (10|20|30|40|50) = volumeControl() Wait(100) {$1_$2} Repeat(2, Wait(100) {esc});

#system volume up = SendSystemKeys({VolumeUp});

brightnessControl() := SendSystemKeys({win+i}) {Down_4} Wait(200) {Right_2} {enter};
brightness control = brightnessControl();
brightness (up|down) (10|20|30|40|50) = brightnessControl() Wait(100) {$1_$2} Repeat(2, Wait(100) {esc});

soundPanel() := SendSystemKeys({Win+r}) WaitForWindow("Run","",1000) "mmsys.cpl"{enter} WaitForWindow("Sound","",1000) {ctrl+down};
Sound panel          = soundPanel();

# index from bottom
<sound_device> := (headset=0 | laptop=1 | soundtouch=2 | Andrea=3);
#<up_down> := (Up="Right" | Down="Left");
#<adjust_amount> := (tiny=2 | small=5 | medium=10 | large=20 | massive=40);

## bring up volume control of the specified device
#levelAdjust(deviceindex) := soundPanel() {Down_$deviceindex} {Alt+p} {Ctrl+Tab};

Sound to <sound_device> = soundPanel() {Down_10} Repeat($1, Wait(100) {up})
    Wait(100) {Alt+s} {enter};
#volume <up_down> <adjust_amount> <sound_device> = levelAdjust($3) {$1_$2}
#                                                  Repeat(2, {enter});
#volume (mute | unmute) <sound_device> = levelAdjust($2) {Tab} {Space}
#                                        Repeat(2, {enter});

# specific action for soundtouch, connect and set as default
Sound connect [to] soundtouch = soundPanel() {Down_10} Wait(200) {up_2} Wait(100) 
    {shift+f10} Wait(100) {down_2} Wait(100) {enter} Wait(2000) {alt+s} Wait(100)
    {esc};

Sound disconnect [from] soundtouch = soundPanel() {Down_10} Wait(100) {up_2} 
    Wait(100) {shift+f10} Wait(100) {down_4} Wait(100) {enter} {esc};

displayPanel() := SendSystemKeys({Win+r})  "desk.cpl"{enter} WaitForWindow(
"Control Panel\All Control Panel Items\Display\Screen Resolution","",2000);
display (settings|panel)          = displayPanel();

#deviceControl() := 
#    controlPanel() Wait(1000) "dev" {right} {enter} WaitForWindow("Devices and Printers","",2000);

#massStorageEject() :=
#    deviceControl() Wait(2000) "Mass"  {Alt+f} {e};


#Device control      = deviceControl();
#eject mass storage = massStorageEject();
networkPanel() := SendSystemKeys({Win+r}) "ncpa.cpl"{enter} {ctrl+down};
Network panel          = networkPanel();

commandPrompt() := SendSystemKeys({Win+r}) "cmd.exe"{enter};
command panel  = commandPrompt();

adminCommandPrompt() := SendSystemKeys({Win+s}) "cmd.exe" Wait(400)
    {shift+f10} Wait(400) {up_2} Wait(400) {enter};
# so commands don't seem to get loaded or some other problem that means
# we can't dictate into window
# command panel = adminCommandPrompt();

adminScriptsExecute(file_name) := adminCommandPrompt() Wait(1000)
    "c:\win^ scripts\" "$file_name"{enter} Wait(1000) "exit"{enter};

scriptsExecute(file_name) := commandPrompt() Wait(1000)
    "c:\win^ scripts\" "$file_name"{enter} Wait(1000) "exit"{enter};

# bring up VM, putty terminals and mount NFS share. this doesn't require manual
# authentication as with accessing using "file ..." unimacro grammar
load chroma machine  = scriptsExecute("_first_VM.bat");
load second chroma machine  = scriptsExecute("_second_VM.bat");

# bring down all VMs and unmount NFS shares
close virtual machines = scriptsExecute("_stop_headless.bat");

disable local area connection = adminScriptsExecute("_disable_local_area_connection.bat");
enable local area connection = adminScriptsExecute("_enable_local_area_connection.bat");
# ---------------------------------------------------------------------------
# global text shortcuts

hypertext = "http://";
secure hypertext = "https://";

(bite code=pyc|
	python=py|
	Shell=sh|
	text=txt|
	tar=tar.gz|
	jason=json) extension = ".$1 ";

Keyac (space|
	backspace|
	page up=pgup|
	page down=pgdn|
	control="ctrl"|
	alt|
	shift|
	del|
	source="src"|
	escape="esc"|
	pie="py"|
    red package="rpm"|
    standard="std"|
    string="str"|
	config="cfg") = "$1";

<key_short> := (
  pie="python"|
  interactive pie="ipython"|
  upper pie="PYTHON"|
  Hydra="HYD-"|
  Corrie="corosync"|
  chrome="chroma");
keyboard <key_short> = $1;

(vim | bash) config                   = ".$1rc";
insert signature = "{enter}{enter}Regards,{enter}Tom";
double right arrow = ">> ";
triple quote = '"""';
python interpreter = "python ";
root user = "root";
as root = "sudo ";
default prefix = "192.168.";
(BEGIN|END) separator = "----$1----{enter}";
firefox advanced settings = "about:preferences#advanced";

# editor custom text
# this is to enable processes running in supervisor on Guest to connect to
# remote debugger running on host (pycharm listening on 2100 on host)
# Gateway putty session, first VM putty session and VirtualBox port forwarding
# rules allow this to work
(import|insert) Pie (develop|debug) = "import pydevd;pydevd.settrace('imldev.local', port=2100, stdoutToServer=True, stderrToServer=True)";
# local debug on calling commandline
import debug = "import ipdb;ipdb.set_trace()";

[(upper)] she said = When($1, "ZFS", "zfs");
[(upper)] she pool = When($1, "ZfsPool", "zpool");
[(upper)] she data = When($1, "ZfsDataset", "dataset");
