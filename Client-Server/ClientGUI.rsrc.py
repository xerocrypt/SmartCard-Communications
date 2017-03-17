{'application':{'type':'Application',
          'name':'Template',
    'backgrounds': [
    {'type':'Background',
          'name':'bgClientGUI',
          'title':u'Client Interface',
          'size':(506, 256),
          'foregroundColor':(87, 255, 87),
          'backgroundColor':(68, 68, 68),
          'style':['resizeable'],

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'StaticText', 
    'name':'lblStatus', 
    'position':(10, 195), 
    'backgroundColor':(237, 236, 235, 255), 
    'font':{'style': 'bold', 'faceName': u'Liberation Sans', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(87, 255, 87, 255), 
    'text':u'Status:', 
    },

{'type':'StaticText', 
    'name':'lblClient', 
    'position':(12, 9), 
    'backgroundColor':(237, 236, 235, 255), 
    'font':{'style': 'bold', 'faceName': u'Liberation Sans', 'family': 'sansSerif', 'size': 14}, 
    'foregroundColor':(87, 255, 87, 255), 
    'text':u'Messaging Client', 
    },

{'type':'StaticText', 
    'name':'lblMessage', 
    'position':(10, 99), 
    'backgroundColor':(237, 236, 235, 255), 
    'font':{'style': 'bold', 'faceName': u'Liberation Sans', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(87, 255, 87, 255), 
    'text':u'Message:', 
    },

{'type':'StaticText', 
    'name':'lblRemoteIP', 
    'position':(10, 51), 
    'backgroundColor':(237, 236, 235, 255), 
    'font':{'style': 'bold', 'faceName': u'Liberation Sans', 'family': 'sansSerif', 'size': 11}, 
    'foregroundColor':(87, 255, 87, 255), 
    'text':u'Server IP:', 
    },

{'type':'Button', 
    'name':'cmdSend', 
    'position':(400, 45), 
    'backgroundColor':(102, 102, 102, 255), 
    'foregroundColor':(87, 255, 87, 255), 
    'label':u'Send', 
    },

{'type':'TextField', 
    'name':'txtStatus', 
    'position':(90, 189), 
    'size':(397, -1), 
    'backgroundColor':(87, 255, 87, 255), 
    },

{'type':'TextArea', 
    'name':'txtMsg', 
    'position':(90, 88), 
    'size':(394, 87), 
    'backgroundColor':(87, 255, 87, 255), 
    },

{'type':'TextField', 
    'name':'txtAddr', 
    'position':(90, 47), 
    'size':(298, -1), 
    'backgroundColor':(87, 255, 87, 255), 
    },

] # end components
} # end background
] # end backgrounds
} }
