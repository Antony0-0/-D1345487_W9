def recommend_videos():
    n = int(input("請輸入影片的總數："))
    videos = []
    for _ in range(n):
        data = input().split()
        name = data[0] 
        viewers = int(data[1]) 
        avg_watch_time = int(data[2]) 
        video_length = int(data[3]) 
        relevance = int(data[4])
        priority_index = viewers * avg_watch_time * video_length * relevance
        videos.append((name, priority_index))
    videos.sort(key=lambda x: x[1], reverse=True)
    for video in videos:
        print(video[0])
recommend_videos()