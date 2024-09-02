const user = {
    name: "Piyush Sharma",
    designation: "Senior Software Engineer",
    company: "Infuse Consulting",
    hobbies: [ "Reading","Listening to music", "Collecting stamps"]
}

const printUserProfile = () => {
    // Piyush Sharma is a Senior Software Engineer at Infuse Consulting. He likes Reading, Listening to music and Collecting stamps
    let {name, designation,company,hobbies}=user;
    const len=hobbies.length;
    const [firstHalf, secondHalf] = [hobbies.slice(0, len-1), hobbies.slice(len-1)];
    console.log(`${name} is a ${designation} at ${company}. He likes ${firstHalf} and ${secondHalf}`);
}

printUserProfile()
