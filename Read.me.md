Big Data Analytics Homework1
工管碩一 M10401003 廖韋茹

  此次作業內容以抓取Twitter資料為主，擷取到的資料皆儲存成json格式，所上傳之zip檔分別如下。
    
    1. Community Website_1：內含以關鍵字"Facebook"及"baidu"關鍵字為主之json檔。
    2. Community Website_2：內含以關鍵字"Instagram"及"Weibo"關鍵字為主之json檔。
    3. Musical instrument：內含以關鍵字"piano"及"violin"關鍵字為主之json檔。
    4. Taiwan：內含以關鍵字"Taiwan"及"ROC"關鍵字為主之json檔。
    5. animation：內含以關鍵字"animation"關鍵字為主之json檔。
    6. emotion：內含以關鍵字"love"及"hate"關鍵字為主之json檔。
    7. terrorism_1：內含以關鍵字"ISIS"及"terrorist"關鍵字為主之json檔。
    8. terrorism_2：內含以關鍵字"terror attack"關鍵字為主之json檔。
  
  共八個zip壓縮檔，以下將介紹擷取到的json檔欄位及擷取資料之來源與主題。

A. 資料架構 
  
  本次所儲存的資料架構皆為json檔，以下將以欄位中較為重要之部分欄位進行解釋其意義：

    1. contributors：此欄位內容主要包含發文者之資料，如ID、Username等等。
    2. text：為發文者所張貼之內容。
    3. entities：為發文者張貼內容所包含的符號或URL等。
    4. retweeted：指原發文者所張貼之內容是否有被其他Twitter使用者回推，即該文章是否有被其他使用者轉載或重發。
    5. source：即該關鍵字所擷取的資料來源。

B. 資料來源

  a. API
    以Twitter API為主要來源，所查詢的關鍵字分別為："baidu"、"Facebook"、"Weibo"、"Instagram"、"animation"、"hate"、"love"、"piano"、"violin"、"ISIS"、"terror attack"、"terrorist"、"Taiwan"、"ROC"。

  b. 內容主題與查詢字串
    
    將本次作業所查詢到之內容與查詢字串條列如下所示。
    
    1. Community Website
      以社群網站為主題, 以Instagram、baidu、Weibo及Facebook等有名社群網站為主，希望能夠找出，在Twitter上，其他何種社群網站也是曝光度及出現度較高之關鍵字，也能夠知道哪些Twitter使用者也同時在使用著第二種社群網站

    2. Musical instrument
      以樂器為主題，以piano及violin兩種樂器為主，因為此兩種樂器分別被稱為樂器之王及樂器之后，為大多數音樂學習者的首要選擇之一，所以希望能夠透過資料的擷取與分析，得知在Twitter這個社群網站上面，鋼琴及小提琴分別被討論及提出的次數誰多誰寡。

    3. Taiwan
      以台灣為主題，分別透過Taiwan及ROC(Repblic of China)等兩種關鍵字來做查詢，希望能夠透過討論內容的分析，得知目前台灣在國際中最主要被討論的議題為何、台灣最受到注目的部份為何，也同時能夠瞭解台灣及中華民主共和國哪個名稱較常被提及。

    4. animation
      以動畫為主題，希望能夠知道目前最受到注目及討論的動畫為何，及其被討論內容為何，並藉此得知國際間動畫界的變化及趨勢。

    5. emotion
      以"love"和"hate"為關鍵字進行查詢，love及hate為兩個意思相反且較為極端的詞彙，hate屬於非常負面的動詞，且love為非常正面的動詞，希望能夠透過兩個字彙在Twitter上的出現比例得知，Twitter上較多的是較為正面還是負面的內容，也能夠進一步分析出使用者大多是在正面或者是負面的情緒下選擇Twitter做為宣洩的管道，或想分享的內容大多數是以正向或負向為主。

    6. terrorism
      進年來多起恐怖攻擊事件頻傳，其中又以ISIS為主要來源，所以查詢的關鍵字以"ISIS"、"terrorist"及"terror attack"三個關鍵字為主，希望能夠分析出在Twitter上最主要被討論的恐怖攻擊相關內容有哪些。