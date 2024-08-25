const user = {
    name: "Piyush Sharma",
    designation: "Senior Software Engineer",
    company: "Infuse Consulting",
    hobbies: ["Reading", "Listening to music", "Collecting stamps"]
}

let {name, designation,company,hobbies}=user;
const len=hobbies.length;
console.log(len);
const firstSetHobbies=hobbies.slice(0,len-1).join(",");
const LastHobbies=hobbies.slice(len-1);

const printUserProfile = () => {
    // Piyush Sharma is a Senior Software Engineer at Infuse Consulting. He likes Reading, Listening to music and Collecting stamps
    
    console.log(`${name} is a ${designation} at ${company}. He likes ${firstSetHobbies} and ${LastHobbies}`);
}

printUserProfile()
