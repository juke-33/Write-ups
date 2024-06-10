# Vinegar Times 3

## We can't speak French and just say what we see.

## We also don't know what underscores are add them yourself.

## put ONLY the final decrypted cipher in bcactf{}, no intermediate steps

## key - vinegar

## cipher 0 - mmqaonv

## cipher 1 - seooizmt

## cipher 2 - bdoloeinbdjmmyg

So i found that this is Vigenere Cipher.

So first decoded cipher 0 with the key and got: redwine

Next i decoded cipher 1 with redwine as a key and got: balsamic

Last i decoded cipher 2 with balsamic as a key and got: addtosaladyummy

Flag: `bcactf{add_to_salad_yummy}`