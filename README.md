# KeyDeck
The KeyDeck is a custom designed macropad that is semi-based on the [Hackpad]([url](https://hackpad.hackclub.com)) tutorial. I used KiCad to create a custom schematic and pcb for my own macropad, then I used Onshape to cad everything from the case to the full assembly of the KeyDeck, I researched the parts from many different sellers and decided on the best ones, and wrote some alpha firmware for the main controller. I made this project because I always have wanted to make a Hack Club project but never found the right one for me. I can say that I originally just wanted to make a simple HackPad but now this has evolved into something more, something that helped me learn many useful software and engineering skills too along the way. This project isn't very complex or anything extremely special, but i'm proud of it because of the skills I learned.

# CAD Link:
https://cad.onshape.com/documents/f0da09f9133df872021c7bb6/w/39fd902933bfae87f6640d91/e/d6283e9f59527cd2ccb38ed5  
(A bit messy, but serves it's job)
# KeyDeck Renders:
<img width="1920" height="1080" alt="cornerRender-min" src="https://github.com/user-attachments/assets/3d2408cd-2d05-4712-8007-ee0b47e680b3" />
Corner Shot


<img width="1920" height="1080" alt="sideRender-min" src="https://github.com/user-attachments/assets/f694990f-a2dd-456b-9288-c83020f53e7b" />
Side View


<img width="1920" height="1080" alt="topRender-min" src="https://github.com/user-attachments/assets/b989dd2b-79cf-4bed-bdd1-eb9f737e958c" />
Top Down


# KeyDeck CAD Images:
<img width="1740" height="1108" alt="image" src="https://github.com/user-attachments/assets/a7ca5d36-e787-4f4d-b3bf-d4e812cc1b80" />
Top Angle


<img width="986" height="424" alt="image" src="https://github.com/user-attachments/assets/26c17cd1-8fb9-4371-be2a-533baeb2b819" />
Top Down

# KeyDeck PCB

<img width="755" height="372" alt="Screenshot 2025-07-31 at 12 42 20 AM" src="https://github.com/user-attachments/assets/4c282726-4cec-441d-a8e9-6135dceeb1c5" />
  
PCB Schematic

<img width="1898" height="862" alt="image" src="https://github.com/user-attachments/assets/df5e19f8-0431-40a4-9a2e-3f1177650193" />
PCB Cad With A Few Components

# KeyDeck BOM

| Name:                                     | Description:                                                                                                                                                                                                                                                                                                                                                                                                                       | Quantity: | Final Price: | Link: |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------ | ----- |
| Cherry MX Red Switches                    | Keyswitches to be used on the KeyDeck. These are not official but are price optimized from Aliexpress. Should serve the same puurpose just fine. I have to have the full price because the $0.99 discount is the LEDs, which is more expensive overall. Tax and Shipping for both LEDs and Switches included in the LEDs price because the actual product was cheaper. Decided to get a few extra incase I break any in assembly.  | 20        | $8.74        | [AliExpress](https://www.aliexpress.us/item/3256806069646359.html?spm=a2g0o.productlist.main.2.724a3474MZWkEA&algo_pvid=737d6045-fe2a-482a-ba36-cc2cdf85aea5&algo_exp_id=737d6045-fe2a-482a-ba36-cc2cdf85aea5-1&pdp_ext_f=%7B"order"%3A"1022"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21USD%215.99%210.99%21%21%2143.01%217.14%21%402103244817542682999465243e2fa1%2112000036489552472%21sea%21US%216279080118%21ABX&curPageLogUid=tzxadgPFfUvE&utparam-url=scene%3Asearch%7Cquery_from%3A)  |
| KeyDeck PCB                               | PCB for the project. Had to order the minimum quantity which was 5. Coupon for $6 applied to make it extra cheap.                                                                                                                                                                                                                                                                                                                  | 5         | $3.50        | N/A   |
| Seeed Studio RP2040 XIAO                  | The main controller for the KeyDeck. Might be Backordered but that's alright. Using the pre-soldered version as I decided on manual assembly.                                                                                                                                                                                                                                                                                      | 1         | $13.76       | [Seeed Studio](https://www.seeedstudio.com/Seeed-Studio-XIAO-RP2040-Pre-Soldered-p-6333.html)  |
| SK6812 (Neopixel) LEDs                    | LEDs for the KeyDeck PCB. Minimum Quantity I could find was 100. Discount is applied on this one to make it $0.99 instead of the switches because this one is more expensive overall. Tax and Shipping for both Switches and LEDs included in this price.                                                                                                                                                                          | 100       | $4.31        | [AliExpress](https://www.aliexpress.us/item/3256807802380183.html?spm=a2g0o.productlist.main.3.3f24sYiDsYiDPe&algo_pvid=6ad03e82-cb50-4483-96eb-f1ae26d5de71&algo_exp_id=6ad03e82-cb50-4483-96eb-f1ae26d5de71-2&pdp_ext_f=%7B"order"%3A"15"%2C"eval"%3A"1"%7D&pdp_npi=4%40dis%21USD%2114.04%210.99%21%21%21100.82%217.11%21%40210313e917542746935784900eafd9%2112000043173268003%21sea%21US%216279080118%21ABX&curPageLogUid=ol3pGnDxLFVO&utparam-url=scene%3Asearch%7Cquery_from%3A)  |
| KeyDeck Case                              | This includes the base/body + lid. This case was designed to be 3D-Printed. I have a 3D-Printer and will be manufacturing all parts of this type myself.                                                                                                                                                                                                                                                                           | 1         | None         | N/A   |
| Keycaps                                   | The current keycaps on the cad are fine. I will 3D-Print these myself, removing the cost. In the future, I plan to make custom keycaps that are multi-color and have different logos on them to correspond to different shortcuts that they indicate. For now, stock keycaps are fine.                                                                                                                                             | 8         | None         | N/A   |
| 8-32 0.25in. Hex Drive Button Head Screws | The screws to be used to assemble the KeyDeck case. I have some, so no cost.                                                                                                                                                                                                                                                                                                                                                       | 4         | None         | [McMaster Carr](https://www.mcmaster.com/97763a176/)  |
| Total Cost:                               |                                                                                                                                                                                                                                                                                                                                                                                                                                    |           | $30.31       |       |
