from langchain import hub

# pulling prompt from my hub 
prompt = hub.pull("riphunter7001x/custom-template-for-blog-generation")


# it conatiain prompt \
#     prompt = f"""
# As an experienced blog writer, generate a blog based on the given topic and infomation. Ensure the blog follows this structure:

# Heading:
# Clearly define the topic of the blog.

# Introduction:
# Provide an engaging introduction to the topic.

# Content:
# Present detailed and informative content, supported by research and relevant sources.

# Summary:
# Summarize the main points covered in the blog.

# from given infomation only
# """