import hashlib
import struct

pii_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris vulputate posuere vestibulum. Sed tincidunt lectus tortor, sit amet euismod nunc scelerisque ac. Pellentesque cursus turpis urna, ut feugiat nisi porta eget. Morbi vitae nisi et nisi facilisis accumsan non id dolor. Mauris velit dui, eleifend ac consequat in, rutrum non eros. Pellentesque mollis lacus in neque pulvinar blandit. Praesent tempor, nunc et commodo tincidunt, ipsum ex sagittis est, non lobortis ante dui vitae sapien. Aliquam at ligula placerat, cursus risus sit amet, varius erat. Maecenas at orci at justo mollis dignissim. Nam egestas nec ex et pulvinar. Curabitur molestie urna non congue fringilla. Sed pulvinar, sem feugiat ultrices laoreet, velit nulla iaculis diam, tempus sodales quam odio nec leo.

Maecenas at est massa. Vivamus vel tellus vehicula, volutpat massa sit amet, gravida orci. Phasellus euismod luctus nunc, sed congue nulla tincidunt at. Duis quam turpis, volutpat sit amet odio vel, volutpat iaculis nulla. Proin venenatis libero eget malesuada consectetur. Phasellus sit amet ex rhoncus mi suscipit ornare. Donec sed rutrum ipsum, ut egestas turpis. Nullam id leo at nulla posuere ultrices vitae vel tortor. Cras in tellus neque. Sed elit libero, ornare id urna sed, viverra malesuada nisl.

Praesent lobortis felis eget mi suscipit, non ultrices nisi tincidunt. Pellentesque tincidunt mauris eget purus molestie porttitor. Sed enim lectus, ultricies non facilisis interdum, iaculis a orci. Phasellus luctus nec ante sit amet suscipit. Ut tempus lectus eget risus sagittis, a maximus nulla facilisis. Proin at molestie lectus. Quisque fringilla nunc eget libero dapibus, eget maximus ex dignissim. Integer porta egestas eleifend.

Nullam imperdiet orci vitae felis aliquam eleifend. Aenean blandit dignissim tellus nec facilisis. Duis ac urna risus. Vestibulum tempus condimentum justo, id dapibus nulla maximus ut. Sed sed accumsan justo. Interdum et malesuada fames ac ante ipsum primis in faucibus. Sed luctus fermentum ligula, ut ultricies lacus fringilla a.

Ut consequat dui arcu, bibendum condimentum eros mattis eu. Nam sed massa porttitor, convallis dolor at, suscipit leo. Curabitur vitae tortor ac mi malesuada auctor in malesuada diam. Etiam lacinia nulla felis, fermentum elementum diam blandit sit amet. Praesent eu molestie arcu. Sed et ornare eros. Proin id eros nisl. Etiam pulvinar at metus ac fermentum.
"""

pii_bytes = pii_text.encode('utf-8')

python_string_hash = ''.join(format(x,'02x') for x in struct.pack('>q', hash(pii_text)))


hashes = {}
hashes['python-internal-hash'] = python_string_hash
hashes['md5'] = hashlib.md5(pii_bytes).hexdigest()
hashes['sha1'] = hashlib.sha1(pii_bytes).hexdigest()
hashes['sha224'] = hashlib.sha224(pii_bytes).hexdigest()
hashes['sha256'] = hashlib.sha256(pii_bytes).hexdigest()
hashes['sha384'] = hashlib.sha384(pii_bytes).hexdigest()
hashes['sha512'] = hashlib.sha512(pii_bytes).hexdigest()

for k in sorted(hashes.keys()):
    print(f"{k:<24} len: {len(hashes[k])>>1: >6,} bytes; hash: {hashes[k]}")
