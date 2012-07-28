tvp-dl
======

Just returns download URL of videos from tvp.pl which uses damn silverlight. Fun! Fun! Fun!

Hints:
------
1. Generated URL is only IP-specific. No cookies/user-agent checks.
2. All (debug) informations beside actual download URL are thrown into stderr, so tricks like ``mplayer `python tvp-dl.py ...` `` does work just fine.
3. TVP.pl *does* allow ~~downloading~~ watching videos from other countries (at least from Roubaix/France ;))

tvp-dl (tym razem po polskiemu)
===============================

Zwraca URL do pobrania wideo z tvp.pl, które korzysta z cholernego silverlight'a. Fun! Fun! Fun!

Wskazówki:
----------
1. Wygenerowane URLe są jedynie unikalne per-IP. Żadnych testów user-agent czy ciastek.
2. Wszystkie informacje (debug) oprócz samego URLa do pobrania wysyłane są na stderr, także tricki w stylu ``mplayer `python tvp-dl.py ...` `` po prostu działają.
3. TVP.pl *pozwala* na ~~pobieranie~~ oglądanie klipów w innych krajach (przynajmniej w Roubaix/Francja)

Examples/Przykłady:
----------
		python tvp-dl.py http://www.tvp.pl/styl-zycia/magazyny-sniadaniowe/pytanie-na-sniadanie/muzyka/wystep-taneczny-weroniki-grycan-i-lukasza-paciorka/8057459
		python tvp-dl.py http://londyn2012.tvp.pl/8109625/dobrowolski-pokazalem-naszym-jak-powinno-sie-to-robic

TODO:
-----
1. Server sometimes returns NOT_AUTHORIZED status (i've got no idea why)

