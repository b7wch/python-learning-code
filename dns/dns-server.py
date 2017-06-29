import socket


class DNSQuery:
    def __init__(self, data):
        self.data = data
        self.dominio = ''

        tipo = (ord(data[2]) >> 3) & 15  # Opcode bits
        if tipo == 0:  # Standard query
            ini = 12
            lon = ord(data[ini])
            while lon != 0:
                self.dominio += data[ini + 1:ini + lon + 1] + '.'
                ini += lon + 1
                lon = ord(data[ini])

    def respuesta(self, ip):
        packet = ''
        if self.dominio:
            packet += self.data[:2] + "\x81\x80"
            packet += self.data[4:6] + self.data[4:6] + '\x00\x00\x00\x00'  # Questions and Answers Counts
            packet += self.data[12:]  # Original Domain Name Question
            packet += '\xc0\x0c'  # Pointer to domain name
            packet += '\x00\x01\x00\x01\x00\x00\x00\x3c\x00\x04'  # Response type, ttl and resource data length -> 4 bytes
            packet += str.join('', map(lambda x: chr(int(x)), ip.split('.')))  # 4bytes of IP
        return packet


if __name__ == '__main__':
    ip = ['192.168.1.1', '192.168.1.2', '192.168.1.3', '192.168.1.4', '192.168.1.5']
    print 'pyminifakeDNS:: dom.query. 60 IN A %s' % ip

    udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udps.bind(('', 53))
    ip_index = 0
    try:
        while 1:
            if ip_index > len(ip) - 1:
                ip_index = 0
            data, addr = udps.recvfrom(1024)
            p = DNSQuery(data)
            udps.sendto(p.respuesta(ip[ip_index]), addr)
            print 'Respuesta: %s -> %s' % (p.dominio, ip)
            ip_index += 1
    except KeyboardInterrupt:
        print 'Finalizando'
        udps.close()
