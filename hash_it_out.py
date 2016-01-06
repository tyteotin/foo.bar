def answer(digest):
    # modulo 256 return right most 8 bits, don't care about the rest.
    # XOR current digest with previous message returns current message after multiply by 129.
    # x * 129 = x * (128+1) = x * (2^7) + x = (x << 7 + x).
    # (x << 7) moves LSB to MSB in the 8 bits. 
    # Adding (x << 7) to x flips the MSB of x based on value of LSB.
    
    # If LSB of x is 1, flip MSB, else no flipping. Only keep right most 8 bits 
    msg = digest[0] ^ 0
    digest[0] = (msg ^ 128)%256 if (msg & 1) else msg%256

    for i in range(1, len(digest), 1):
        msg = digest[i] ^ digest[i-1]
        digest[i] = (msg ^ 128)%256 if (msg & 1) else msg%256
    return digest
