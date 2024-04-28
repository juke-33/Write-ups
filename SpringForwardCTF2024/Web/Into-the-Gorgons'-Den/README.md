## Into-the-Gorgons'-Den

### Whether she was Hesiod's disfigured monstrous mortal or Ovid's cursed and abused fair maiden--Medusa and her Gorgon sisters must be stopped. If not we shall all be turned to stone! Enter their lair, learn your surroundings, and find a way...
### Provided Link: https://springforward-into-the-gorgons-den.chals.io/

- Solution

If we inspect the page we can notice this script:
```
<script>
	function getMirrorClue() {
        var fragments = ["minus 2.",
            "She will turn her gaze at the 30th minute ",
            "is her reflection!  ",
			"weakness ",
			" Medusa's ",
			"The hidden clue is: ",
		];

		var clue = "";

		for (var i = 4; i >= 0; i--) {
			clue += fragments[i];
		}

		return clue;
	}

	function mirror() {
		var input = document.getElementById("mirrorInput").value;
		var output = document.getElementById("mirrorOutput");

		if (input.toLowerCase() === "suesrep") {
			var clue = getMirrorClue();
			output.innerHTML = clue;
			output.style.display = "block";
        }

        else {
            output.innerHTML = input.split("").reverse().join("");
            output.style.display = "none";
        }
    }
</script>
```

We put the word "suesrep" in the Mirror Input and we get this result
```
Medusa's weakness is her reflection! She will turn her gaze at the 30th minute minus 2.
```

Then we have a text that can be decoded using ROT13 and we get this:
```
The second part of the flag is the but the e is a 3 !
```

After all these we put "sl4yth3" in the last input and we get the flag format:
```
function checkInput() {
	var input = document.getElementById('flagInput').value;
	var secretPhrase = 'sl4yth3';

	if (input === secretPhrase) {
		fetchFlag();
	} else {
		alert('Incorrect input. Please try again.');
	}
}
```

Finally we put all the parts together. I didn't manage to get the first part...

Flag: nicc{part1_th3_g0rg0n}