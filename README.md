# ten-bis balance cli util

### get your currently ten-bis balance from your terminal in 1.157 seconds!

![url=https://ibb.co/yNn5PhY](https://i.ibb.co/D1DkWG8/example.png)


#### example: 
```
~$ tenbis
Uses the credential file on: .tenbis_cli.txt

Welcome to the TenBis panel!
your monthly frame is ₪359.50 / 880.00
the balance is 510.50
```
## Advantages:
#### you just wanna know how much of money left to spend on this mounts you not need -->
- to login!
- to open browser the middle of your important work over the terminal!
- to navigate over the slow and frustrating ten-bis website and menus!

just get your balance at any time in the easiest way that passable!


## setup:
### only 3 minutes of setup and lifetime of happiness!
- get your ten-bis cookie:
    1. open your favorite browser, and open the inspect-tool, and select the monitoring section (see below picture fig1)
    2. open [ten-bis user report page](https://www.10bis.co.il/Account/UserReport)
    3. over the network menu, filter "UserReport" in the filter box, and select Doc over the response type (see picture fig2)
    4. right-click on the "UserReport" response, and select "copy as CURL"  (see picture fig3)
    5. paste it in some text-editor, and copy the value after  `-H 'cookie: ` until the end of the line
- paste the value in a new file on this path "~/.tenbis_cli.txt" 
- You are good to go! 

#### the picture:
![figures to get the cookie](https://i.ibb.co/PNFn0Df/figs.png)
