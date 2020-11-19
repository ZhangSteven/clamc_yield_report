# clamc_yield_report

Here is the API description.

## getReturnDataFromPositions()
[Boolean] withCash, [Int] cutoffMonth, [Float] impairment, [Iterator] positions => [Float] realized return, [Float] total return

A function to get realized return and total return value from investment positions, Where

1) withCash: a boolean indicator, True means the scenario with cash, False otherwise;
2) cutoffMonth: an integer value. For example, if it is 5, then any month on or before 5 is in case 1, otherwise case 2;
3) impairment: a float value.
4) positions: positions from an investment position report.


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
