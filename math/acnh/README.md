#Animal Crossing New Horizons Event Items Profit Math

##### Contents:
- [Wedding Event](#wedding-event)
    - [Heart Crystals](#heart-crystals)
    - [Obtainable Items](#obtainable-items)
    - [Getting the Most Profitable Items](#getting-the-most-profitable-items)
    - [Local Setup](#local-setup)

# Wedding Event

The Wedding Event in ACNH runs from June 1st to June 30th in 2020. The event invites a user to
Harv's Island where they decorate a room to Reese and Cyrus's request. They then take a picture to
show it off. Showing the picture to Reese will reward the user with a variable amount of Heart
Crystals based on how well they followed the furniture request. These requests change every day of
the event, whether it is Cyrus making more furniture for the user to use or requiring the user to
use color-customized versions of Cyrus' created furniture. The user can then trade their obtained
Heart Crystals into Cyrus for some of the furniture and other items used in the decorating stage of
the event. The items obtained from trading Heart Crystals can be used for decoration/wear or it can
be sold for a potential profit.

## Heart Crystals

For the first seven days of the event, the maximum number of Heart Crystals a user can get per day
is twelve. The remaining 23 days of the event, the maximum number of Heart Crystals a user can get
per day is fifteen. The maximum number of Heart Crystals a user can get on their own is 429. That is
`(7 days * 12 crystals/day) + (23 days * 15 crystals/day)`.

Heart Crystals can be sold for 100 bells each, but there is certain furniture that can be traded for
a maximum profit of 650 bells per Heart Crystal.

## Obtainable Items

Item Name                    | HCR* | Sell Price | Ratio**
---------------------------- | ---- | ---------- | -------
Wedding Pipe Organ           |   40 |      25000 |    6.25
Wedding Table                |    6 |       1500 |    2.50
Wedding Flower Stand         |    4 |       1000 |    2.50
Wedding Arch                 |   20 |       5000 |    2.50
Cake Dress                   |   20 |       5000 |    2.50
Wedding Cake                 |    5 |       1000 |    2.00
Wedding Bench                |    5 |        875 |    1.75
Wedding Chair                |    3 |        500 |    1.67
Wedding Tuxedo               |   20 |       3000 |    1.50
Wedding Shoes                |    6 |        750 |    1.25
Wedding Pumps                |    6 |        750 |    1.25
Wedding Head Table           |    6 |        750 |    1.25
Bridal Veil                  |   12 |       1150 |    0.96
Rugs (Blue, Red, White)      |    4 |        375 |    0.94
Wedding Decoration           |    3 |        250 |    0.83
Wedding Welcome Board        |    5 |        375 |    0.75
Wedding Candle Set           |    4 |        300 |    0.75
Walls (Brown, Green, White)  |   12 |        750 |    0.62
Floors (Brown, Green, White) |   12 |        750 |    0.62
Wedding-party Wall           |   12 |        473 |    0.36

* HCR: Heart Crystal Ratio.
** The ratio of the Sell Price to Number of Heart Crystals.

## Getting The Most Profitable Items

In order to only focus on profit in calculating a user's maximum profit based on the number of Heart
Crystals they have, every item that has a ratio equal to or less than 1 is not included in the list
of potential items to trade for. It would be more profitable to sell the Heart Crystals themselves
instead of those items.

Items such as Cake Dress, Wedding Bench, Wedding Cake, Wedding Tuxedo, Wedding Shoes, Wedding Pumps,
and Wedding Head Table are also not included in the list of potential items due to the fact that
they will never be returned as potential items. They will never be returned due to the sorting the
calculations do to the obtainable items. All items are sorted in descending order, first by the
Ratio, then by the number of Heart Crystals, then by Item Name. This leaves 5 profitable items that
will be evaluated.

Item Name                    | HCR* | Sell Price | Ratio**
---------------------------- | ---- | ---------- | -------
Wedding Pipe Organ           |   40 |      25000 |    6.25
Wedding Arch                 |   20 |       5000 |    2.50
Wedding Table                |    6 |       1500 |    2.50
Wedding Flower Stand         |    4 |       1000 |    2.50
Wedding Chair                |    3 |        500 |    1.67

## Local Setup

### Dependencies

[Python 3.8.3](https://www.python.org/downloads/release/python-383/)

Optional, for running the test suite:
[Pytest 5.4.2](https://pypi.org/project/pytest/)

### Commands

If you would like to run the method locally, clone this repo and run the following commands from the
top level directory:

```
cd math/acnh
python3 -c 'from best_wedding_items import get_best_wedding_items; items = get_best_wedding_items(); print(items)'
```
The command line will then ask you to input how many Heart Crystals you have to trade. Once input,
it will print out the items you should trade for, along with their amounts, in order to gain the
most profit.

You can also run the test suite to ensure that everything is working as intended, if you wish.

Install Dependencies:
``` python3 -m pip install pytest ```

Test:
``` pytest -v ```

