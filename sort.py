import heapq

def sort_large_file(file_path, output_path, chunk_size):
    with open(file_path, 'r') as input_file:
        chunk = []
        for line in input_file:
            number = int(line.strip())
            chunk.append(number)
            if len(chunk) == chunk_size:
                chunk.sort()  # 内部排序
                write_chunk(chunk, output_path)
                chunk = []
        
        if chunk:
            chunk.sort()  # 最后剩余的数据块排序
            write_chunk(chunk, output_path)

def write_chunk(chunk, output_path):
    with open(output_path, 'a') as output_file:
        output_file.write('\n'.join(str(number) for number in chunk) + '\n')

def merge_sorted_files(file_paths, output_path):
    with open(output_path, 'w') as output_file:
        chunks = []
        chunk_pointers = []

        # 初始化每个文件的指针和对应的数据块
        for file_path in file_paths:
            file = open(file_path, 'r')
            chunk = file.readlines()
            chunks.append(chunk)
            chunk_pointers.append(0)
        
        # 使用堆来选择最小的元素合并到输出文件
        heap = []
        for i, chunk in enumerate(chunks):
            number = int(chunk[0].strip())
            heap.append((number, i))
        
        heapq.heapify(heap)

        while heap:
            smallest, file_index = heapq.heappop(heap)
            output_file.write(str(smallest) + '\n')
            pointer = chunk_pointers[file_index] + 1

            if pointer < len(chunks[file_index]):
                next_number = int(chunks[file_index][pointer].strip())
                heapq.heappush(heap, (next_number, file_index))
                chunk_pointers[file_index] = pointer
            else:
                chunks[file_index] = []
        
        # 关闭所有文件
        for chunk in chunks:
            if chunk:
                file.close()
                break

sort_large_file('phone_numbers.txt', 'output.txt', chunk_size=100000)
merge_sorted_files(['output.txt'], 'sorted_output.txt')