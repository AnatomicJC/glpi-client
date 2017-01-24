glpi-client
===========

Python client to interact with GLPI webservices plugin

---

glpi-client provides 2 clients to interact with GLPI webservices plugin:

 - XMLRPC client (preferred)
 - REST Client

####Usage:####

    from glpi_client.XMLRPCClient import XMLRPCClient
    glpi = XMLRPCClient('http://localhost/glpi')
    glpi.connect('login', 'password')

From this glpi object, you can call all GLPI webservices methods listed on this page: https://forge.glpi-project.org/projects/webservices/wiki/En_devguide

For each webservices method, you can use python help() method

#### Examples: ####

**glpi.getObject** method (https://forge.glpi-project.org/projects/webservices/wiki/GlpigetObject):

    help(glpi.getObject)
    
Will give you this output:

    Help on function getObject in module glpi_client.XMLRPCClient:
    getObject(module='glpi', **kwargs)
    Wrapper for GLPI webservices getObject method:
        It could be a good idea to see method's reference page:
        https://forge.glpi-project.org/projects/webservices/wiki/GlpigetObject
    @param module: webservices module to call (default: glpi)
    @type module: str
    @param kwargs: options for getObject method:
            - with_softwareversion: bool
            - with_document: bool
            - show_label: bool, optional
            - with_ticketvalidation: bool
            - with_peripheral: bool
            - help: bool,optional
            - with_infocom: bool, optional
            - with_contract: bool
            - show_name: bool, optional
            - with_tickettask: bool
            - with_ticketfollowup: bool
            - with_software: bool
            - with_networkport: bool, optional
            - with_reservation: bool
            - with_softwarelicense: bool
            - with_printer: bool
            - with_monitor: bool
            - with_ticket: bool
            - id: integer
            - with_phone: bool, optional (Computer only)
    @type kwargs: dict

Then, use it !

    glpi.getObject(
        itemtype='Computer',
        id=290,
    )
    
On my GLPI install, it provides this result:

    {'autoupdatesystems_id': '1',
    'computermodels_id': '1',
    'computertypes_id': '1',
    'contact': 'jc',
    'date_mod': '2014-02-13 09:50:20',
    'domains_id': '1',
    'entities_id': '1',
    'groups_id': '0',
    'groups_id_tech': '0',
    'id': '290',
    'locations_id': '0',
    'manufacturers_id': '1',
    'name': 'trinity',
    'networks_id': '0',
    'operatingsystems_id': '1',
    'operatingsystemservicepacks_id': '0',
    'operatingsystemversions_id': '11',
    'serial': 'R9PZ865',
    'states_id': '1',
    'users_id': '0',
    'users_id_tech': '0',
    'uuid': '10F82C81-5267-11CB-863F-DC00B89EBF52'}

**glpi.updateObjects** method (https://forge.glpi-project.org/projects/webservices/wiki/GlpiupdateObjects):

    help(glpi.updateObjects)
    
Will give you this output:

    Help on function updateObjects in module glpi_client.XMLRPCClient:
    updateObjects(module='glpi', **kwargs)
    Wrapper for GLPI webservices updateObjects method:
    It could be a good idea to see method's reference page:
    https://forge.glpi-project.org/projects/webservices/wiki/GlpiupdateObjects
    @param module: webservices module to call (default: glpi)
    @type module: str
    @param kwargs: options for updateObjects method:
        - fields: array, mandatory
        - help: bool, optional
    @type kwargs: dict

Then, use it !

    update_info = {
        'Computer': [
            {
                'id':'6793',
                'states_id' : '16'
            }
        ]
    }
    result = glpi.updateObjects(fields=update_info)
