class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        valid_ip_addresses = []

        def is_valid_ip_address(ip_address_parts: list):
            if len(ip_address_parts) != 4:
                return False
            for part in ip_address_parts:
                if part == "":
                    return False
                if len(str(int(part))) != len(part):
                    return False
                if not (0 <= int(part) <= 255):
                    return False
            return True

        n = len(s)

        def recursion(index, dots_left, ip_address):
            if dots_left == 0:
                ip_address[-1] += s[index:]
                if is_valid_ip_address(ip_address):
                    valid_ip_addresses.append('.'.join(ip_address))
                return
            if index > n-1:
                return
            # do add the dot
            recursion(
                index+1, dots_left - 1, 
                ip_address + [s[index]]
            )
            # do not add the dot
            old = ip_address[-1]
            new = old + s[index]
            ip_address[-1] = new
            recursion(index+1, dots_left, ip_address)
            ip_address[-1] = old

        recursion(0, 3, [""])
        return(valid_ip_addresses)

            
                
            