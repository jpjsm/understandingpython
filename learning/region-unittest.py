import unittest
import region

class TestRegion(unittest.TestCase):

    def test_constructor(self):
        # validate constructor elements: name, shortname, aliases
        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', 'phx')
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, 'r2',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1', 'r2', 'phx'])) and (len(rgn.aliases) == 3))

        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', '')
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, 'r2',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1', 'r2'])) and (len(rgn.aliases) == 2))

        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', None)
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, 'r2',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1', 'r2'])) and (len(rgn.aliases) == 2))

        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', '', 'phx')
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, '',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1','phx'])) and (len(rgn.aliases) == 2))

        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', None, 'phx')
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, '',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1','phx'])) and (len(rgn.aliases) == 2))

        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', ['phx','px','p1'])
        self.assertEqual(rgn.name, 'us-phoenix-1',"Name different in constructor")
        self.assertEqual(rgn.shortname, 'r2',"Shortname different in constructor")
        self.assertTrue((rgn.aliases <= set(['us-phoenix-1','r2','phx','px','p1'])) and (len(rgn.aliases) == 5))
        # end of: validate constructor elements: name, shortname, aliases
        
        # validate constructor rejects invalid values
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region('', 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region(None, 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region('123', 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region(123, 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region('_us-phoenix-1', 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region('us-phoen!x-1', 'r2', 'phx')
        
        region.regions.clear()
        region.region_index.clear()
        with self.assertRaises(AssertionError):
            rgn = region.Region('us-phoenix-', 'r2', 'phx')
        # end of: validate constructor rejects invalid values

        # validate constructor adds information to static dictionaries: regions, region_index
        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', ['phx','px','p1'])
        self.assertTrue(region.regions.has_key(rgn.name.lower()), "'us-phoenix-1' name not in regions dictionary")
        self.assertEqual(region.regions[rgn.name.lower()], rgn,"Object in regions dictionary different then constructed")
        self.assertTrue(region.region_index.has_key(rgn.shortname.lower()), "'r2' alias not in region_index dictionary")
        self.assertEqual(region.region_index[rgn.shortname.lower()], rgn.name.lower(),"'r2' alias not referencing 'us-phoenix-1'")
        for alias in rgn.aliases:
            self.assertTrue(region.region_index.has_key(alias), "Alias not in region_index dictionary")
            self.assertEqual(region.region_index[alias], rgn.name.lower(),"Alias not referencing 'us-phoenix-1'")
        # end of: validate constructor adds information to static dictionaries: regions, region_index

        # validate constructor checks static dictionaries before constructing a new instance
        region.regions.clear()
        region.region_index.clear()
        rgn = region.Region('us-phoenix-1', 'r2', ['phx','px','p1'])
        with self.assertRaises(AssertionError):
            rgn2 = region.Region('us-phoenix-1', 'r2', 'phx')
            rgn3 = region.Region('us-seattle-1', 'r2', 'sea')
            rgn4 = region.Region('us-seattle-1', 'r1', 'p1')
        #checking nothing is left behind from incomplete constructs
        self.assertFalse(region.regions.has_key('us-seattle-1'),"'Name' from incomplete construct was created.")
        self.assertFalse(region.region_index.has_key('us-seattle-1'),"Alias from incomplete construct was created.")
        self.assertFalse(region.region_index.has_key('sea'),"Alias from incomplete construct was created.")
        self.assertFalse(region.region_index.has_key('r1'),"Alias from incomplete construct was created.")
        
        # end of: validate constructor checks static dictionaries before constructing a new instance
        
    # end of: TestConstructor

# End of unit tests
if __name__ == '__main__':
    unittest.main()    