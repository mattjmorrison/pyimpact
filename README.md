# Python ImpactJS Development Webserver

This egg is heavily based on amadeus' server.py for which none of this would be possible.

Thanks amadeus

https://github.com/amadeus/python-impact

## Disclaimer

Use this in a production environment at your own risk.  In fact it is heavily discouraged to deploy
your ImpactJS game being served by this webserver.

## Usage

To get up and running with the python impactjs webserver all you will need to do is:

    pip install pyimpact

After you've installed pyimpact, from the command line, type

    startimpact --host=<HOSTNAME> --port<PORT>

The command line arguments are strictly optional and will default to:

    host: 'localhost'
    port: '8080'

### Tip

Change the --host=0.0.0.0 if you'd like to access your game across a local network.

### Testing

`python setup.py test`
