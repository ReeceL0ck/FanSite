
const API_KEY = 'RGAPI-baefd220-b28d-4850-91ec-ca8de7e859e8';
const REGION = 'EUW1';
const PUUID = 'e8sf3At2fL0HC54833IgRhDRGy3uslK9ubjxQibVn2rZoG9bpzv1yzoMLK4BZeOW3XFFcEO6UMd3zg';


async function getSummonerRank(puuid = PUUID, region = REGION) {
    const url = `https://${region}.api.riotgames.com/lol/league/v4/entries/by-puuid/${puuid}`;
    
    console.log(`Fetching data from: ${url}`);
    try {
        const response = await fetch(url, {
            headers: {
                'X-Riot-Token': API_KEY
            }
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        return data[1];
    } catch (error) {
        console.error('Error fetching summoner rank:', error);
        throw error;
    }
}

function processSummonerRankData(data) {
    if (data.length === 0) {
        console.log('No rank data found for this summoner.');
        return;
    }

    queueType = data.queueType;
    rank = data.tier +' '+ data.rank;
    win_rate = (data.wins / (data.wins + data.losses) * 100).toFixed(2);
    leaguePoints = data.leaguePoints;
    const el = document.getElementById("rank-display");
    const el2 = document.getElementById("hot-streak");
    if (win_rate > 50) {
        el.classList.add("above-50");
        el.classList.remove("below-50");
    } else {
        el.classList.add("below-50");
        el.classList.remove("above-50");
    }
        if (data.hotStreak == true) {
        el2.classList.add("above-50");
        el2.classList.remove("below-50");
    } else if (data.hotStreak == false) {
        el2.classList.add("below-50");
        el2.classList.remove("above-50");
    }
    document.getElementById('rank-display').textContent = `${rank} ${win_rate}%`;
    document.getElementById('hot-streak').textContent = data.hotStreak ? 'Yes' : 'No';

}



getSummonerRank(PUUID, REGION)
    .then(data => {
        processSummonerRankData(data);
    })
    .catch(error => {
        console.error('Error:', error);
    }); 


const videoFiles = [
    'kindred.mp4',
    'taliyah.mp4',
];  

function getRandomVideo() {
    const randomIndex = Math.floor(Math.random() * videoFiles.length);
    return videoFiles[randomIndex];
}

function updateVideoContainer() {
    const videoContainer = document.querySelector('.video-container');
    const randomVideo = getRandomVideo();
    
    videoContainer.innerHTML = `
        <h3 class="video-title">Now playing: ${randomVideo}</p>
        <video width="800" height="600" controls>
            <source src="src/${randomVideo}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
        
    `;
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('Loading random video...');
    updateVideoContainer(); // This picks and plays a random video
    addNextVideoButton();
});