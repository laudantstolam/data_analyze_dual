### Result Preview

![image.png](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402191546709.png)

### Intro

Inspired by several Spotify expanded third-party project that expand into visualizing various listening data in well-designed interfaces, but limited to the analysis of personal data. Consequently, I decided to develop a project based on the concept of "making friends through music" to compare the data of two individuals. By analyzing personal listening habits, trending artists, and song attributes, we could present several types of data analysis.

本次專題是鑒於平時經常使用Spotify收聽音樂以及對於將自己的收聽資料視覺化十分感興趣，因此選擇Spotify API結合網頁前端設計來實作出不一 樣的資料視覺呈現。 網路上有許多Spotify衍伸第三方數據可視化的先例，但都僅限個人資料的呈現，因此本次想透過雙人資料的比對，以”以樂會友”的概念發想進行設計，圍繞兩個人的收聽習慣、追蹤藝人、歌曲特色進行數據處理與呈現

### Framework and Workflow

![image.png](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402191546086.png)

### Data Processing Detail

#### 1. Music Genere Preference 近期收聽種類

![image.png|213](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402191549525.png)
##### TIME RANGE : 6 months
##### APIs
- `Get User's Top Items`
##### PROCESS
- Call API to get user's top 50 trend artist's genere
- Calculate the top generes that's repeated more that 5
##### MEANING
- visulize the music genere preference and percentage

#### 2. Trending Artist 近期收聽藝人

![image.png|255](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402192151449.png)
##### TIME RANGE : 4 weeks
##### APIs
- `Get User's Top Artists`
##### PROCESS
- Call API to get get user’s top 3 artists' link and profile image
##### MEANING
- present what we are listening to recently

#### 3. Music Feature Analyzing 音樂特徵分析

![image.png|375](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402192205653.png)

##### TIME RANGE : 4 weeks
##### APIs
- `Get User's Top Tracks`
- `Get audio features`
##### PROCESS
- Call API to get user’s top 50 tracks
- Call API to get tracks' feature
- Calculate and normalize the result
- Compare the closest values and generate music taste
##### MEANING
- turning numerical features into words to get better understand of the result
- visulize extract parameter and compare on radar chart to observe

#### 4. Generated Recommend Playlist

![image.png|375](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402192244063.png)

##### APIs
- `Get Recommendations`
##### PROCESS
- Calculate the average of each features from 4.(audio features)
- Passing into the API and generate a recommend playlist to display
##### MEANING
- Base on the analysis of the audio feature and further create a playlist to discover with friends
- Explore simillar tastes songs with friends
#### 5. Current Track & Preview

![image.png|247](https://raw.githubusercontent.com/Ash0645/image_remote/main/202402192241777.png)

##### APIs
- `Get Current Track`
##### PROCESS
- Call API to get currently playong track and their demo
##### MEANING
- share what are you listening with friends

