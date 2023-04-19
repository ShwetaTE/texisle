console.log("hey from about page");
var form = new FormData();
form.append("title", "Frequency Of Update");
form.append("app", "TEST");
form.append("chart", "TS");
form.append(
  "message",
  "  All individual tickers under Steel Manufacturing, Pipe Manufacturing, and Mining Companies are updated every hour. All spot prices as well as the Index under Raw Materials gets updated daily by 9:30 am CT. For Transportation, BADI gets updated daily by 9:30 am CT, USLD gets updated every week by Friday 9:30 am CT, Truck Transportation and Cass Freight gets updated by the second week of each month. All futures data for spot prices and USLD in Transportation are updated once every day by 9:30 am CT. Index charts for Pipe Manufacturing, Steel Manufacturing and Mining Companies are updated every hour. Currently, the Transportation Index shows a general combined view of all transportation trends. All data associated with Rig count is updated every week on Monday by 9:00 am CT. Well Count is updated by 7:00 am CT of next business day after the new data is available on original source. All curated articles with calculated relevance are updated twice every day, 6:30 am CT &amp; 11:30 am CT. All curated tweets with calculated relevance &amp; filtered with relevancy AI are updated every 4 hours"
);
const fetchData = async () => {
  // console.log("heey");
  const response = await fetch(urlresource + `/createMessage/`, {
    method: "POST",
    body: form,
  });
  console.log("responseee", response);
  const data = await response.json();
  console.log(data);
};
// fetchData();
const getData = async () => {
  const response = await fetch(urlresource + "/getMessage/");
  const data = await response.json();
  // console.log(data);
  if (data.length) {
    const about = data.filter((e) => e[0] == "about");
    // console.log(about[0][1]);
    // console.log(document.querySelector(".about_Dynamic"));
    document.querySelector(".about_Dynamic").innerHTML = about[0][1];
  }
  if (data.length) {
    const faq = data.filter((e) => e[0] == "FAQ1");
    // console.log(faq[0][1]);
    // console.log(document.querySelector(".about_Dynamic"));
    document.querySelector(".faq_Dynamic_1").innerHTML = faq[0][1];
  }
  if (data.length) {
    const faq = data.filter((e) => e[0] == "FAQ2");
    // console.log(faq[0][1]);
    // console.log(document.querySelector(".about_Dynamic"));
    document.querySelector(".faq_Dynamic_2").innerHTML = faq[0][1];
  }
  if (data.length) {
    const faq = data.filter((e) => e[0] == "FAQ3");
    // console.log(faq[0][1]);
    // console.log(document.querySelector(".about_Dynamic"));
    document.querySelector(".faq_Dynamic_3").innerHTML = faq[0][1];
  }
  if (data.length) {
    const ref = data.filter((e) => e[0] == "REF");
    // console.log(ref[0][1]);
    // console.log(document.querySelector(".about_Dynamic"));
    document.querySelector(".ref_Dynamic").innerHTML = ref[0][1];
  }
};
getData();
