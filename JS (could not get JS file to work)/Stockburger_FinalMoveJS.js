function Stockburger_FinalMoveJS() {

  function JeweleryDesign(){
    const month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const price = [25, 30, 20, 80, 75, 60, 70, 40, 70, 60, 50, 30];
    const stone = ["Garnet", "Amethyst", "Aquamarine", "Diamond", "Emerald", "Pearl", "Ruby", "Peridot", "Sapphire", "Opal", "Topaz", "Turquois"]
    var monthBirth;
    var convertStone;
    let selectedMonths = [];
    let totalStonePrice = 0;
    let totalPurchase = 0;
    let necklace = 100;
    
      
    document.write("Order Summary: " + "\n");
    
    
    while (true) {
      monthBirth = prompt("Enter a month to add a birthday gemstone. Please type full word and capitalize to avoid errors. You can enter \"done\" when finished.");
      if(monthBirth === "done") {
        break;
      }
     
      const monthIndex = month.indexOf(monthBirth);
      if(monthIndex !== -1) {
      selectedMonths.push(monthBirth);
      
      

      document.write(month[monthIndex] + " was added to the order." + "\n");
      } else {
      document.write("You had an invalid entry. Please try again." + "\n");
      }

      
     } 
     
     
     document.write("You entered " + selectedMonths.length + " birthday stone months." + "\n");
     document.write("\n");
     document.write("Price for each gemstone: " + "\n");
     for(index = 0; index < selectedMonths.length; index++) {
      document.write(stone[index] + " is $" + price[index] + "\n");
      totalStonePrice += price[index];
     }
     
     totalPurchase = (necklace + totalStonePrice);
     
     document.write("Total price for gemstone(s): $" + totalStonePrice + "\n");
     document.write("Total order price is: $" + totalPurchase + "\n");
     document.write("\n");
     document.write("Thank you for your order!");
  }

  JeweleryDesign(); 
  
Stockburger_FinalMoveJS();
}