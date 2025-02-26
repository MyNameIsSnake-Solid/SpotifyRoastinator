// general use

function clearPage()
{
    const elements = document.querySelectorAll("*");

    // console.log(elements.length);
    
    for (x = 0; x < elements.length; x++)
    {
        console.log(elements[x]);
        elements[x].remove();
    }
}

function removeElement(element_to_delete) 
{
    element_to_delete.remove();
}

function wait(seconds) {
    return new Promise(resolve => setTimeout(resolve, seconds * 1000));
  }

// loading screen
async function loopAction(paragraphElement)
{
    // console.log(paragraphElement + " " + paragraphElement.innerHTML);
    count = 0;
    while (true){
        paragraphElement.innerHTML = "Loading";

        for (x = 0; x < count; x++){
            paragraphElement.innerHTML += ".";
        }
        // console.log(count);

        await wait(1);
        count++;
        if (count >= 4)
            count = 0;
    }
}