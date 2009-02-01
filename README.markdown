# JiwaiLaconicaProxy

JiwaiLaconicaProxy is a web server that give you a [Laconica API](http://laconi.ca/trac/wiki/TwitterCompatibleAPI) for accessing the [Jiwai.de](http://jiwai.de) data.

The proxy makes you benefit from the great deal of [Laconica Apps](http://laconi.ca/trac/wiki/Apps).

## What does it look like

You could open the [twhirl](http://www.twhirl.org), add a laconi.ca such as: you_jiwai_account@jiwai.geowhy.org and connect. Then you will able to access your [Jiwai.de](http://jiwai.de) data using [twhirl](http://www.twhirl.org) via JiwaiLaconicaProxy hosted in jiwai.geowhy.org.

## License

This code is copyright (c) 2009 by tsing and is available under the [MIT](http://www.opensource.org/licenses/mit-license.php). See `LICENSE.txt` from details.

## Dependencies

* [Twisted](http://www.twistedmatrix.com) 8.1.x or later

## Run your own instance

Copy `JiwaiLaconica.tac.sample` to `JiwaiLaconica.tac`. Then lauch it with  twistd.
    
    twistd -y JiwaiLaconica.tac

