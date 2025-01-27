async function loadVideos() {
  const response = await fetch("/videos");
  const videos = await response.json();
  const feed = document.getElementById("video-feed");

  videos.forEach((video) => {
    const videoElement = document.createElement("div");
    videoElement.innerHTML = `
            <h3>${video.title}</h3>
            <video controls width="300" src="${video.url}"></video>
            <p>Likes: ${video.likes}</p>
            <button onclick="likeVideo(${video.id})">Like</button>
        `;
    feed.appendChild(videoElement);
  });
}

async function likeVideo(videoId) {
  await fetch(`/like/${videoId}`, { method: "POST" });
  alert("Video liked!");
  location.reload(); // Reload the page to refresh data
}

loadVideos();
