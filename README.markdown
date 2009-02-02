# JiwaiLaconicaProxy

JiwaiLaconicaProxy is a web server that give you a [Laconica API](http://laconi.ca/trac/wiki/TwitterCompatibleAPI) for accessing the [Jiwai.de](http://jiwai.de) data.

The proxy makes you benefit from the great deal of [Laconica Apps](http://laconi.ca/trac/wiki/Apps).

## What does it look like

I'm running a JiwaiLaconicaProxy at jiwai.geowhy.org. 

Here are the instructions how to add a jiwai.de account to twhirl using the proxy hosted at jiwai.geowhy.org, taken from [twhirl blog](http://blog.twhirl.org/2008/09/12/twhirl-preview-for-laconica-sites/):

* open the accounts dialog (click on the top left hand twhirl icon in a twhirl window)
* select `laconi.ca` from the drop-down list at the bottom left hand corner
* enter your username and the JiwaiLaconicaProxy domain as your screen name. Example: to add the account `twhirl` on the http://jiwai.geowhy.org, you would need to enter `twhirl@jiwai.geowhy.org`. Don't include the http:// part, just use the domain name
* Press Return or click the "+" button to add the account
* select the new account in the list and click on `Connect` to open a window for this account


## License

This code is copyright (c) 2009 by tsing and is available under the [MIT](http://www.opensource.org/licenses/mit-license.php). See `LICENSE.txt` from details.

## Dependencies

* [Twisted](http://www.twistedmatrix.com) 8.1.x or later

## Run your own instance

Copy `JiwaiLaconica.tac.sample` to `JiwaiLaconica.tac`. Then lauch it with  twistd.
    
    twistd -y JiwaiLaconica.tac

