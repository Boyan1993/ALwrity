"""Patch for fastapi_clerk_auth to fix Python 3.9 compatibility issues."""

import sys

def patch_fastapi_clerk_auth():
    """Patch fastapi_clerk_auth to fix Python 3.9 type annotation issues."""
    try:
        module_path = "/Users/zhaoshiyu/Library/Python/3.9/lib/python/site-packages/fastapi_clerk_auth/__init__.py"
        
        # Read the original module source
        with open(module_path, 'r') as f:
            source = f.read()
        
        # Replace Python 3.10+ type annotations with Python 3.9 compatible ones
        patched_source = source.replace('str | None', 'Optional[str]')
        patched_source = patched_source.replace('dict | None', 'Optional[dict]')
        patched_source = patched_source.replace('int | None', 'Optional[int]')
        patched_source = patched_source.replace('float | None', 'Optional[float]')
        patched_source = patched_source.replace('bool | None', 'Optional[bool]')
        
        # Write the patched source back
        with open(module_path, 'w') as f:
            f.write(patched_source)
        
        print(f"Successfully patched fastapi_clerk_auth at {module_path}")
        return True
    except Exception as e:
        print(f"Failed to patch fastapi_clerk_auth: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    patch_fastapi_clerk_auth()