window.addEventListener('DOMContentLoaded', (event) =>{
    getVisitCount(); // when content is loaded go run this event
})

const functionAPI = ""
// create a function to get the count
const getVisitCount = () => {
    let count = 30;
    // get the response of the api and return as a json
    fetch(functionAPI).then(Response => {
        return Response.json()
    }).then(Response =>{
        console.log("Website called function API"); // log for debugging
        count = Response.count; // set count variable with the json response 
        document.getElementById("counter").innerHTML = count //set element in the html document to the count
    }).catch(function(error){ // if there is an error lo to the console
        console.log(error);
    });
    return count
}


