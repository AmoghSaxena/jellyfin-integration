# Jellyfin Media Server with Integration

This project sets up a media server using Jellyfin, integrated with Jellyseerr, Sonarr, Radarr, and other related services using Docker Compose.

## Prerequisites

- Docker
- Docker Compose

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/AmoghSaxena/jellyfin-integration.git
    cd your-repo-name
    ```

2. **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add the following content:

    ```env
    # ENV file for docker-compose.yml

    PUID=0
    PGID=0
    TZ=Etc/UTC

    # Ports
    RADARR_PORT=8925
    SONARR_PORT=8926
    PROWLARR_PORT=8927
    FLARESOLVERR_PORT=8928
    QBITTORRENT_PORT=8929
    JELLYSEER_PORT=8930
    JELLYFIN_PORT=8096

    # Volumes
    RADARR_CONFIG=./jellyfin/radarr
    SONARR_CONFIG=./jellyfin/sonarr
    PROWLARR_CONFIG=./jellyfin/prowlarr
    FLARESOLVERR_CONFIG=./jellyfin/flaresolverr
    QBITTORRENT_CONFIG=./jellyfin/qBittorrent
    JELLYSEER_CONFIG=./jellyfin/jellyseer
    JELLYFIN_CONFIG=./jellyfin/jellyfin
    MOVIES_VOLUME=./MountOneDrive/JellyfinData/movies
    TVSERIES_VOLUME=./MountOneDrive/JellyfinData/tvseries
    DOWNLOADS_VOLUME=./jellyfin/downloads
    ```

3. **Run Docker Compose:**

    ```sh
    docker-compose up -d
    ```

    This command will start all the services defined in the [docker-compose.yml](http://_vscodecontentref_/1) file.

## Services

- **Jellyfin**: Main media server for streaming and managing media collections.
- **Jellyseerr**: Request management and media discovery tool for Jellyfin.
- **Sonarr**: Manages TV series collections.
- **Radarr**: Manages movie collections.
- **Prowlarr**: Manages indexers for Usenet and BitTorrent.
- **FlareSolverr**: Bypasses Cloudflare protection.
- **qBittorrent**: BitTorrent client.

## Accessing the Services

- **Jellyfin**: `http://localhost:${JELLYFIN_PORT}`
- **Jellyseerr**: `http://localhost:${JELLYSEER_PORT}`
- **Sonarr**: `http://localhost:${SONARR_PORT}`
- **Radarr**: `http://localhost:${RADARR_PORT}`
- **Prowlarr**: `http://localhost:${PROWLARR_PORT}`
- **qBittorrent**: `http://localhost:${QBITTORRENT_PORT}`

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.
