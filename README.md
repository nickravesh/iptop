# iptop

**Keep it simple, keep it cool. Your go-to for hassle-free IP exploration.**

![iptopGif](https://github.com/nickravesh/iptop/blob/master/assets/demo.gif)

### The Backstory of iptop

> As a frequent user of VPNs, my IP address is in a constant state of flux. Regularly needing to verify my IP details or investigate other IP addresses, I found the existing methods cumbersome. Opening multiple websites for this task felt inefficient. That's when iptop was born—a command-line tool tailored to my needs. Now, checking and inspecting IP information is as simple as a command, reflecting my preference for a seamless, command-line experience.

## Features

- **IP Address Lookup:** Quickly inspect detailed information about a specific IP address by providing it as an argument.

- **Public IP Information:** If no specific IP is provided, iptop defaults to fetching and displaying information about your public IP address.

- **Beautiful Output Design:** Visually pleasing and well-organized display of IP details. The output includes a country flag and information such as country, region, city, continent, ISP, timezone, latitude, longitude, and ASN.

For detailed usage instructions, see the [Usage](#usage) section below.

## One-Liner install

```bash
  curl -Ls https://github.com/nickravesh/iptop/archive/master.tar.gz | tar -xz && cd iptop-master && bash install.sh
```

## Usage
| **Arguments** | **Description** | **Example** |
|:----------------:|-----------------|-------------|
| -ip [ip-address] | Custom IP Lookup | iptop -ip 8.8.8.8 |
| -h/--help | display program help | iptop --help |

**Note:** Without using any arguments, iptop will lookup your own public IP address.

## Contributing	

Contributions are always welcome!  
Let me know if you have any suggestions, or open an issue if you have faced any problems.

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://opensource.org/licenses/)

[![](https://visitcount.itsvg.in/api?id=iptop&label=Repository%20Views&icon=0&pretty=true)](https://visitcount.itsvg.in)