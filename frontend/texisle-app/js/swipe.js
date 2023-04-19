var spot_name = ['scrap', 'hrc', 'coal', 'iron', 'rmi', 'rio', 'vale', 'sxc', 'bhp', 'io', 'ts', 'vkpa', 'x', 'tmst', 'nwpx', 'pm', 'mt', 'pkx', 'nue', 'stld', 'rs', 'clf', 'tx', 'ggb', 'cmc', 'tkade', 'szgde', 'nippon', 'jfe', 'smf', 'baltic', 'usld', 'ag', 'cf', 'truck', 't', 'ardmore', 'arkoma', 'barnett', 'cana', 'niobrara', 'ford', 'granite', 'haynesville', 'marcellus', 'mississippian', 'permian', 'utica', 'williston', 'rc', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC' ]
var ticker = ['SCRAP', 'HRC', 'COAL', 'IRONORE', 'RMI_index', 'RIO', 'VALE', 'SXC', 'BHP', 'IOM_index', 'TS', 'VKPA', 'X', 'TMST', 'NWPX', 'PMF_index', 'MT', 'PKX', 'NUE', 'STLD', 'RS', 'CLF', 'TX', 'GGB', 'CMC', 'TKADE', 'SZGDE', 'NIPPON', 'JFE', 'SMF_index', 'Baltic', 'ULSD', 'AllGrade', 'CassFreight', 'Truck', 'T_index', 'Ardmore', 'Arkoma', 'Barnett', 'Cana', 'Niobrara', 'Ford', 'Granite', 'Haynesville', 'Marcellus', 'Mississippian', 'Permian', 'Utica', 'Williston', 'RC_index', 'Anadarko_DUC', 'Appalachia_DUC', 'Bakken_DUC', 'Eagle_DUC', 'Haynesville_DUC', 'Niobrara_DUC', 'Permian_DUC', 'DPR_DUC' ]

// document.addEventListener('swiped-left', function(e) {
//     console.log(e.target)
// });

$.each(ticker, function (key, value) {
    let index = ticker.indexOf(value);
    document.addEventListener('swiped-left', function(e) {
        console.log(e.target.title); // the element that was swiped
        if(e.target.id == spot_name[index]+"_val_current" || e.target.id == spot_name[index]+"_val_data" || e.target.id == spot_name[index]+"_val_data_neg" || e.target.id == spot_name[index]+"_val_current_2" || e.target.id == spot_name[index]+"_val_data_2" || e.target.id == spot_name[index]+"_val_data_neg_2" || e.target.title == spot_name[index]+"_div"){
            try{
                val = "WL_"+value+"1"
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'none') {
                    a.style.display = 'flex'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-forward-outline');
                }
                val = "WL_"+value
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'none') {
                    a.style.display = 'flex'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-forward-outline');
                }
            }
            catch{
                val = "WL_"+value
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'none') {
                    a.style.display = 'flex'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-forward-outline');
                }
            }
            
        }
    });

    document.addEventListener('swiped-right', function(e) {
        // console.log(e.target.id); // the element that was swiped
        if(e.target.id == spot_name[index]+"_val_current" || e.target.id == spot_name[index]+"_val_data" || e.target.id == spot_name[index]+"_val_data_neg" || e.target.id == spot_name[index]+"_val_current_2" || e.target.id == spot_name[index]+"_val_data_2" || e.target.id == spot_name[index]+"_val_data_neg_2" || e.target.title == spot_name[index]+"_div"){
            try{
                val = "WL_"+value+"1"
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'flex') {
                    a.style.display = 'none'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-back-outline');
                }
                val = "WL_"+value
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'flex') {
                    a.style.display = 'none'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-back-outline');
                }
            }
            catch{
                val = "WL_"+value
                // console.log(val)
                var a = document.getElementById(val);
                if (a.style.display == 'flex') {
                    a.style.display = 'none'
                    // val1.querySelector('ion-icon').setAttribute('name', 'chevron-back-outline');
                }
            }
        }
    });
});