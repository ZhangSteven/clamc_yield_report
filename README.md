# clamc_yield_report

Here is the API description.

## getPositions()
[String] filename => [Dictionary] metaData, [Iterator] positions

where

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
  pos['Invest'] == 0.00149 (original string is 1.49%, convert to float number)
```
