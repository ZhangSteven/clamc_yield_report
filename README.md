# clamc_yield_report

Here is the API description.

## getPositions()
[String] filename => [Dictionary] metaData, [Iterator] positions

A function to read positions and meta data from an input file, where

1) metaData: a dictionary object containing the following keys:
AccountingRunType, BookCurrency, Portfolio, PeriodEndDate, PeriodStartDate

2) positions: an iterator object representing a collection of positions, where each position is a dictionary object.


### Input File
The input file is a csv file with tab as separator. It is splited into multiple parts by blank lines.

The first part contains holdings data, with the first line as column names and subsequent lines as posiitons, each line representing one position.

The second part contains meta data, with key value separated by tabs. Search for the desired keys in the meta data section, if a key is not found, represent its value by ''.


### Example
```
metaData, positions = getPositions("samples\investment position 2020-07.txt")
```

Then the following should be true:
```
  metaData['AccountingRunType'] == 'ClosedPeriod'
  metaData['BookCurrency'] == 'HKD'
  metaData['Portfolio'] == '12XXXChinaLifeOverseasBondGroup'
  metaData['PeriodEndDate'] == '2020-07-31' (original date string is of format mm/dd/yyyy, change format to yyyy-mm-dd)
  metaData['PeriodStartDate'] == '2020-07-01'
```

Suppose pos is the first element in the positions iterator, then following should be true:

```
  pos['ReportMode'] == 'Investments'
  pos['LongShortDescription'] == 'Cash Long'
  pos['SortKey'] == 'Cash and Equivalents'

  ... any columns between SortKey and MarketValueBook ...

  pos['MarketValueBook'] == 2963497343.25 (original string is "2,963,497,343.25", convert to float number)
  pos['Invest'] == 0.0149 (original string is 1.49%, convert to float number)
```


## getReturnDataFromPositions()
[Boolean] withCash, [Iterator] positions => [Float] realized return, [Float] total return

A function to get realized return and total return value from profit and loss positions, where

1) withCash: a boolean indicator, True means the scenario with cash, False otherwise;
2) positions: positions from an investment position report.


## getNav()
[Boolean] withCash, [Int] cutoffMonth, [Float] impairment, [Dictionary] metaData, [Iterator] positions => [Float] NAV

A function to get NAV from investment positions, where

1) withCash: a boolean indicator, True means the scenario with cash, False otherwise;
2) cutoffMonth: an integer value in [1, 12]. For example, if it is 5 and the "PeriodEndDate" field of the metaData variable is on or before May, then it's case 1, case 2 otherwise;
3) impairment: a fixed number;
4) metaData: meta data of the positions;
5) positions: positions from an investment position report.
