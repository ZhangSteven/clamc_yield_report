# clamc_yield_report

Here is the API description.

## getPosition()
[String] filename => [Dictionary] metaData, [Iterator] holding

where

1) metaData is a dictionary object that contains the following keys:
AccountingRunType, BookCurrency, Portfolio, PeriodEndDate, PeriodStartDate

2) holding is an iterator object representing a collection of positions, where each position is a dictionary object.


### Input File
The input file is a csv file with tab as separator. It is splited into multiple parts by blank lines.

The first part contains holdings data, with the first line as column names and subsequent lines as posiitons, each line representing one position.

The second part contains meta data, with key value separated by tabs. Search for the desired keys in the meta data section, if a key is not found, represent its value by ''.


### Example
file = "investment position 2020-07.txt"
metaData, holding = getInvestmentPosition(file)

Then the following should be true:

  metaData['AccountingRunType'] == 'ClosedPeriod'
  metaData['BookCurrency'] == 'HKD'
  metaData['Portfolio'] == '12XXXChinaLifeOverseasBondGroup'
  metaData['PeriodEndDate'] == '2020-07-31' (original date string is of format mm/dd/yyyy, change format to yyyy-mm-dd)
  metaData['PeriodStartDate'] == '2020-07-01'

Suppose pos is the first element in the holding iterator, then following should be true:

  pos['ReportMode'] == 'Investments'
  po s['LongShortDescription'] == 'Cash Long'
  pos['SortKey'] == 'Cash and Equivalents'

  ... any columns between SortKey and MarketValueBook ...

  pos['MarketValueBook'] == 2963497343.25 (original string is "2,963,497,343.25", convert to float number)
  pos['Invest'] == 0.00149 (original string is 1.49%, convert to float number)

