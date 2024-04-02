import folium

mapOjp = folium.Map(location=(14.160987545426053, 101.39271798051362), zoom_start= 13.5)

# 1st_marker ป่านันทนาการน้ำตกเขาอีโต้
folium.Marker([14.147845387710621, 101.40126250289737],
    tooltip='Click me!', 
    popup=folium.Popup("""
                  <img src="https://www.maengpro.com/wp-content/uploads/2022/10/Club-De-Nuit-Intense-11.jpg" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>ป่านันทนาการน้ำตกเขาอีโต้<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500), 
    icon=folium.Icon(icon='glyphicon glyphicon-tree-deciduous', color='green')).add_to(mapOjp)

# 2nd_marker ป่านันทนาการน้ำตกเขาอีโต้
folium.Marker([14.151150089841666, 101.40971045610237],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://img.wongnai.com/p/1920x0/2022/10/13/516023773d144b19815ef9c0c4cac4a5.jpg" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>น้ำตกเขาอีโต้<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-tint', color='blue')).add_to(mapOjp)

# 3rd_marker อ่างเก็บน้ำเขาอีโต้
folium.Marker([14.153896635355474, 101.40411050796757],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://lh5.googleusercontent.com/p/AF1QipNwbosjSfUMwQVsmZSGMXsTk0SrDwn2t3-Uehkd=w408-h306-k-no" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>อ่างเก็บน้ำเขาอีโต้<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-map-marker', color='red')).add_to(mapOjp)

# 4th_marker จุดถ่ายรูปอ่างเก็บน้ำเขาอีโต้
folium.Marker([14.154656961441514, 101.40678923681747],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://img.wongnai.com/p/1920x0/2019/10/01/2758188221b54e54bb43fa0e60f49dda.jpg" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>จุดถ่ายรูปอ่างเก็บน้ำเขาอีโต้<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-camera', color='lightblue')).add_to(mapOjp)

# 5th_marker จุดชมวิวผาหินซ้อน
folium.Marker([14.145573958343707, 101.38501074478113],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://lh5.googleusercontent.com/p/AF1QipMO_623lTKst7U8T0t_wFLyvGm51voPzPYKoFPW=w408-h306-k-no" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>จุดชมวิวผาหินซ้อน<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-camera', color='lightblue')).add_to(mapOjp)


# 6th_marker พระพุทธทวารวดีศรีปราจีน สิรินทรโลกนาถ
folium.Marker([14.166861579618345, 101.38996755550734],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://lh5.googleusercontent.com/p/AF1QipO4gM5LlGjJPFkJCpCloKFoAU2Gd0iqZNvbY3vq=w408-h305-k-no" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>พระพุทธทวารวดีศรีปราจีน สิรินทรโลกนาถ<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='place-of-worship', prefix='fa', color='gray')).add_to(mapOjp)

# 7th_marker เนินพิศวง
folium.Marker([14.170638053536075, 101.38802420082949],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://lh5.googleusercontent.com/p/AF1QipPsNZvlwFqtvdaKfK6veq_XtiEbFsNlZ3i0Hk_Q=w408-h306-k-no" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>เนินพิศวง<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-camera', color='lightblue')).add_to(mapOjp)

# 8th_marker จุดชมวิวเขาอีโต้
folium.Marker([14.181728025474383, 101.38615485118372],
    tooltip='Click me!',
    popup=folium.Popup("""
                  <img src="https://lh5.googleusercontent.com/p/AF1QipPojji_zcLxotwr-cSnblL087ZATmOR0BFBgrCa=w408-h306-k-no" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>
                  <h4>จุดชมวิวเขาอีโต้<br/></h4>
                  <h5>สอบถามข้อมูลเพิ่มเติม <a href="https://www.facebook.com/khaoeto" target="_blank">ได้ที่นี่</a></h5>
                  """, max_width=500),
    icon=folium.Icon(icon='glyphicon glyphicon-camera', color='lightblue')).add_to(mapOjp)

mapOjp
mapOjp.save("index.html")
