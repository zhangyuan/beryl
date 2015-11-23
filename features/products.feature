Feature: Search Product Feature

Scenario: search product by keyword
   Given Open products page
    when search by keyword "influxdb"
    then only products match the keyword "influxdb" should be shown