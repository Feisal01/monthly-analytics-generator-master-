
import os
# retreive urls from the linkFile
def csv_files_remove():
    with open ('linkFile.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    f.close
    for element in lines:
        os.remove(element.split('/')[-1])
    
    
    
    # csv_files = ['openDataPortal.siteAnalytics.datasetsByOrg.bilingual.csv', 'openDataPortal.siteAnalytics.datasetsByOrgByMonth.bilingual.csv',
    #             'openDataPortal.siteAnalytics.internationalUsageBreakdown.bilingual.csv','openDataPortal.siteAnalytics.provincialUsageBreakdown.bilingual.csv',
    #             'openDataPortal.siteAnalytics.top100Datasets.bilingual.csv','openDataPortal.siteAnalytics.totalMonthlyUsage.bilingual.csv']

csv_files_remove()
