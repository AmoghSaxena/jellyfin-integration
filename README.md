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

    There are two ways to create the `.env` file:

    **Method 1: Copy and Edit Manually**

    Copy the `sample_env.env` file to `.env` and edit the content manually:

    ```sh
    cp sample_env.env .env
    ```

    Open the `.env` file in a text editor and update the values as needed.

    **Method 2: Use the Python Script**

    If you have Python installed on your machine, you can use the provided script to create the `.env` file based on [sample_env.env](http://_vscodecontentref_/1):

    ```sh
    python script_to_create_env.py
    ```

    Follow the prompts to enter the values for each variable. The script will create the `.env` file with the provided values.

3. **Run Docker Compose:**

    ```sh
    docker-compose up -d
    ```

    This command will start all the services defined in the [docker-compose.yml](http://_vscodecontentref_/2) file.

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
- **Jellyseerr**:`http://localhost:${JELLYSEER_PORT}`
- **Sonarr**: `http://localhost:${SONARR_PORT}`
- **Radarr**: `http://localhost:${RADARR_PORT}`
- **Prowlarr**: `http://localhost:${PROWLARR_PORT}`
- **qBittorrent**: `http://localhost:${QBITTORRENT_PORT}`

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.