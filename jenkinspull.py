def jenkinspull(url,pictureName,x1,y1,x2,y2):
    import time
    from selenium import webdriver
    from PIL import Image
    driver = webdriver.PhantomJS('C:/Users/rajpathak/Desktop/Jenkins/PYTHONSCRIPT/phantomjs.exe')
    driver.set_window_size(1368,768 ) # set the window size that you need 
    driver.get(url)
    #wait for Javascript to load
    time.sleep(15)
    #save screenshot
    driver.save_screenshot(pictureName)
    driver.quit()
    
    image = Image.open(pictureName)
    # If image has an alpha channel
    if image.mode == 'RGBA':
                   # Create a blank background image
                    bg = Image.new('RGB', image.size, (255, 255, 255))
                    # Paste image to background image
                    bg.paste(image, (0, 0), image)
                    # Save pasted image as image
                    bg.save(pictureName, "PNG")
    pic = Image.open(pictureName)
    pic = pic.crop((x1,y1,x2,y2))
    pic.save("Cropped"+pictureName,'png')  

jenkinspull('http://localhost:8080/job/Testing/workflow-stage/','emailimage.png',236,146,757,316)