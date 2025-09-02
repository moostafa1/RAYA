# check if the vendor id extracted from WI3 pdf found in the vendors or not

1. Login to system
2. Go to `work items`
3. Select `WI3`
4. Download PDF
5. Extract [`Invoice ID`, `Date`, `Vendor`, `Tax ID`, `City`, `Country`]
6. Return to `home page`

7. Hover over `Vendor` and click `Search for Vendor`
8. Select search by `TaxID`
    - if vendor found:
        - Hover over `Vendors` and select `Add Vendor`
        - Fill the Information using the extracted data previously
        - Return to `home page`, and select `WI3`
        - Click `Update Work Item`, and add the following comment: [`vendor id updated to system`]

    - if vendor not found:
        - Return to `home page`, and select `WI3`
        - Click `Update Work Item`, and add the following comment: [`vendor id rejected [not found on system]`]
