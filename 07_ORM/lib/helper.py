import re
from abc import ABC
class Helper(ABC):
    
    @classmethod
    def pascal_to_camel_plural(cls):
        # Use regex to split the class name at capital letters
        words = re.findall('[A-Z][a-z]*', cls.__name__)
        
        # Join the words with underscores
        camel_case_plural = '_'.join(words).lower()
        
        # Pluralize the last word
        if words:
            last_word = words[-1]
            if last_word.endswith('s') or last_word.endswith('x'):
                camel_case_plural += 'es'
            else:
                camel_case_plural += 's'
        
        return camel_case_plural
    
    @classmethod
    def drop_table(cls, CONN, CURSOR):
        """drops the veterinarian table if it exists"""
        try:
            with CONN:
                CURSOR.execute(
                    f"""
                        DROP TABLE IF EXISTS {cls.pascal_to_camel_plural()};
                    """
                )
            # CONN.commit()
        except Exception as e:
            # CONN.rollback()
            return e
