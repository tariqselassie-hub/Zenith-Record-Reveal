import os

def get_hex_ends(filepath):
    if not os.path.exists(filepath):
        return "File not found", "File not found"
    
    first_16 = ""
    last_16 = ""
    
    with open(filepath, 'r') as f:
        # Get first 16 valid hex chars
        while len(first_16) < 16:
            chunk = f.read(1024)
            if not chunk: break
            for char in chunk:
                if char.lower() in '0123456789abcdef':
                    first_16 += char
                    if len(first_16) == 16: break
        
        # Get last 16 valid hex chars
        f.seek(0, 2)
        pos = f.tell()
        buffer_size = 1024
        while len(last_16) < 16 and pos > 0:
            read_size = min(pos, buffer_size)
            pos -= read_size
            f.seek(pos)
            chunk = f.read(read_size)
            # Filter hex chars from chunk and reverse
            hex_in_chunk = "".join([c for c in chunk if c.lower() in '0123456789abcdef'])
            last_16 = hex_in_chunk + last_16
            if len(last_16) > 16:
                last_16 = last_16[-16:]
                
    return first_16, last_16

p_path = r'c:\Zenith_Backup\Zenith-Manifold\Zenith-Record-Reveal\data\P.hex'
q_path = r'c:\Zenith_Backup\Zenith-Manifold\Zenith-Record-Reveal\data\Q.hex'

p_start, p_end = get_hex_ends(p_path)
q_start, q_end = get_hex_ends(q_path)

print(f"P START: {p_start}")
print(f"P END:   {p_end}")
print(f"Q START: {q_start}")
print(f"Q END:   {q_end}")
