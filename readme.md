### Nudity Classifier
A deployable version of the NudeNet detector at https://github.com/bedapudi6788/NudeNet. (NSFW!!)

Runs as scalable docker container that uses the detector option of the classifier. The 
detector provides a rectangle for each detected piece of nudity, which can help with
UI highlighting and/or censoring scripts.
  
### Usage
* Download the repository.
* docker build .
* Copy the container ID.
* docker run -p 5000:80 <paste container ID>

### Recommended deployment

This is designed to be deployed to a single-processor cloud-based machine.
GPU support is disabled for compatibility reasons.

### Environment Variables

`WORKERS=1`

The number of workers for GUNICORN. Defaults to 1.

#### Credit

Code is directly based off of Beedapudi Praneeth's post here:
https://github.com/bedapudi6788/NudeNet/issues/16#issuecomment-522936659

It has been updated to provide some quality of life improvements and
to use the detector version of the classifier, which isn't available
in the above code snippet.

#### License

Free to use under the GNU General public license and the license for the original NudeNet
https://www.gnu.org/licenses/gpl-3.0.txt
https://github.com/bedapudi6788/NudeNet/blob/master/LICENSE