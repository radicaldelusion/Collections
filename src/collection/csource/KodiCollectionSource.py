from src.collection.CollectionSource import CollectionSource
from src.collection.settings import globalCollection




gss = None
class KodiCollectionSource(CollectionSource):
    def __init__(self, index, collection, kodiFolder, onClick=None, limit=None, customTitle=None, customThumb=None):
        if customTitle is None:
            customTitle = kodiFolder.title
            
        if (customThumb is None) and kodiFolder.thumb:
            customThumb = kodiFolder.thumb
        
        super(KodiCollectionSource, self).__init__(index, collection, kodiFolder, onClick, limit, customTitle, customThumb)
        
        #methods
        self.browseOriginUrl = kodiFolder.browseOriginUrl
        
    
    def updateVideos(self):
        self.videoSource.updateContents()
        
    def updateVideosIfDated(self):
        self.videoSource.updateContentsIfDated()
        
        
    def allVideos(self):
        vSource = self.videoSource        
        if vSource.isEmpty() or vSource.updateFailed():
            return ();
             
        return vSource.videos()
    
    
    
    def onClick(self):
        if not self.css.use:
            return gss.onSourceClickKodi
                        
        return self._onClick if self._onClick else self.css.onSourceClickKodi
        
        
    
            

        
        
        
        
        
        
        




        
def init():
    global gss
    gss = globalCollection.gc().sourcesSettings