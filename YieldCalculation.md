# Yield Calculation

The final output of yield calculation contains 8 columns like below:

Period | Realized Return | Total Return | Average NAV | Realized Return Rate | Total Return Rate
-------|-----------------|--------------|-------------|----------------------|-------------------
2020-01| | | | | |
2020-02| | | | | |
2020-03| | | | | |
XXX    | | | | | |

The meaning of the items are:

Item | Meaning
-----|---------
Realized Return | The accumulated realized return per month from year beginning to now. For the case of 2020 Mar, it means adding up the realized return of 2020 Jan, 2020 Feb and 2020 Mar.
Total Return | Similar to the above, but on total return numbers.
Average NAV | The average of per month NAV since last year end. For the case of 2020 Mar, it means adding up NAV of 2019 Dec, 2020 Jan, 2020 Feb and 2020 Mar, then divide by 4.
Realized Return Rate | Realized Return / Average NAV
Total Return Rate | Total Return / Average NAV
