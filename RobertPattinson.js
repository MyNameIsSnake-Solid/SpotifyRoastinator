function clearPage()
{
    const elements = document.querySelectorAll("*");

    console.log(elements.length);
    
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