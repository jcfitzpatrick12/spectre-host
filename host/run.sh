# Set SPECTREPARENTPATH to the parent directory of this script
export SPECTREPARENTPATH=$(dirname "$(dirname "$(realpath "$0")")")

# Check if the directory $SPECTREPARENTPATH/chunks exists; if not, create it
if [ ! -d "$SPECTREPARENTPATH/chunks" ]; then
    mkdir -p "$SPECTREPARENTPATH/chunks"
fi

# Run the Docker container with GUI support
sudo docker run --name spectre-host-container -it --rm \
    -v $SPECTREPARENTPATH/cfg:/home/spectre/cfg \
    -v $SPECTREPARENTPATH/host/logs:/home/spectre/host/logs \
    -v $SPECTREPARENTPATH/chunks:/home/spectre/chunks \
    -v /dev/shm:/dev/shm \
    spectre-host